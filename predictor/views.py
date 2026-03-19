from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Fixture, Prediction
from .forms import PredictionForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

 
# Home page view
# This simply renders the homepage template.
def home(request):
    return render(request, "predictor/home.html")


# Fixture list view
# Retrieves all fixtures from the database and displays them on the fixture list page.
def fixture_list(request):

    # Fetch all fixtures
    fixtures = Fixture.objects.all()

    # Data we want to send to the template
    context = {
        "fixtures": fixtures
    }

    # Render the template with the fixtures
    return render(request, "predictor/fixture_list.html", context)


# Fixture detail view
# Displays information for a single fixture and shows the prediction form.
def fixture_detail(request, fixture_id):
    # Get the specific fixture by ID
    fixture = get_object_or_404(Fixture, id=fixture_id)

    prediction = None
    user_points = None

    # If the user is logged in, try to get their existing prediction for this fixture
    if request.user.is_authenticated:
        prediction = Prediction.objects.filter(
            user=request.user,
            fixture=fixture
        ).first()

        # Track whether the user already had a prediction before submitting the form
        existing_prediction = prediction is not None

        # If the user has already predicted, calculate points if a result exists
        if prediction:
            user_points = prediction.calculate_points()
    else:
        existing_prediction = False

    # If the form is submitted
    if request.method == "POST" and not fixture.is_locked():
        # Bind form data, using the existing prediction if one already exists
        form = PredictionForm(request.POST, instance=prediction)

        if form.is_valid():
            prediction = form.save(commit=False)

            # Attach logged-in user
            prediction.user = request.user

            # Attach fixture
            prediction.fixture = fixture

            prediction.save()

            # Show a success message depending on whether this was a new prediction or an update
            if existing_prediction:
                messages.success(request, "Prediction updated successfully.")
            else:
                messages.success(request, "Prediction saved successfully.")

            return redirect("fixture_detail", fixture_id=fixture.id)

    else:
        # Display blank form or preload existing prediction
        form = PredictionForm(instance=prediction)

    # Data passed to the template
    context = {
        "fixture": fixture,
        "form": form,
        "prediction": prediction,
        "user_points": user_points,
    }

    # Render the fixture detail page
    return render(request, "predictor/fixture_detail.html", context)

# Leaderboard view
# Calculates total prediction points for each user and displays them in ranking order
def leaderboard(request):

    # Retrieve all registered users from the database
    users = User.objects.all()

    # This list will store the leaderboard results
    leaderboard_data = []

    # Loop through each user to calculate their total points
    for user in users:

        # Get all predictions made by this user
        predictions = Prediction.objects.filter(user=user)

        # Track the total points for this user
        total_points = 0

        # Loop through each prediction and calculate the score
        for prediction in predictions:

            # Use the calculate_points() method from the Prediction model
            points = prediction.calculate_points()

            # If the fixture has a result, points will be returned
            # If not, calculate_points() returns None
            if points is not None:
                total_points += points

        # Add the user and their total score to the leaderboard list
        leaderboard_data.append({
            "user": user,
            "total_points": total_points,
        })

    # Sort leaderboard by total_points in descending order
    # Uses Python's built-in sorted() function with a lambda key
    # Reference: Python documentation - https://docs.python.org/3/library/functions.html#sorted
    leaderboard_data = sorted(
        leaderboard_data,
        key=lambda entry: entry["total_points"],
        reverse=True
    )

    # Send the leaderboard data to the template
    context = {
        "leaderboard_data": leaderboard_data
    }

    # Render the leaderboard page
    return render(request, "predictor/leaderboard.html", context)

@login_required
def my_predictions(request):

    predictions = Prediction.objects.filter(user=request.user).select_related(
        "fixture",
        "fixture__result",
        "fixture__home_team",
        "fixture__away_team",
    ).order_by("fixture__kickoff_datetime")

    # Create lists for grouping
    upcoming_predictions = []
    pending_result_predictions = []
    completed_predictions = []

    # Categorise predictions
    for prediction in predictions:
        fixture = prediction.fixture

        if not fixture.is_locked():
            upcoming_predictions.append(prediction)

        elif hasattr(fixture, "result"):
            completed_predictions.append(prediction)

        else:
            pending_result_predictions.append(prediction)

    # # Temporary debug check
    # print(
    #     len(upcoming_predictions),
    #     len(pending_result_predictions),
    #     len(completed_predictions)
    # )        

    return render(request, "predictor/my_predictions.html", {
        "predictions": predictions,  # keep old one temporarily
        "upcoming_predictions": upcoming_predictions,
        "pending_result_predictions": pending_result_predictions,
        "completed_predictions": completed_predictions,
    })

# Matchweek prediction view
# Handles bulk prediction entry for an entire matchweek
@login_required
def matchweek_predictions(request, matchweek):

    # Retrieve all fixtures for the selected matchweek
    fixtures = Fixture.objects.filter(
        matchweek=matchweek
    ).order_by("kickoff_datetime")

    prediction_forms = []

    if request.method == "POST":

        # Clear all unlocked predictions for this matchweek
        if "clear_matchweek" in request.POST:
            deleted_count = 0

            for fixture in fixtures:
                if fixture.is_locked():
                    continue

                deleted, _ = Prediction.objects.filter(
                    user=request.user,
                    fixture=fixture
                ).delete()

                deleted_count += deleted

            if deleted_count > 0:
                messages.success(
                    request,
                    "Matchweek predictions cleared successfully."
                )
            else:
                messages.info(
                    request,
                    "No unlocked matchweek predictions were available to clear."
                )

            return redirect("matchweek_predictions", matchweek=matchweek)

        all_valid = True

        # Rebuild each form using submitted POST data
        for fixture in fixtures:

            existing_prediction = Prediction.objects.filter(
                user=request.user,
                fixture=fixture
            ).first()

            form = PredictionForm(
                request.POST,
                instance=existing_prediction,
                prefix=f"fixture_{fixture.id}"
            )

            prediction_forms.append({
                "fixture": fixture,
                "form": form,
            })

            if not form.is_valid():
                all_valid = False

        # Only save predictions if every form is valid
        if all_valid:

            for item in prediction_forms:

                fixture = item["fixture"]
                form = item["form"]

                # Prevent predictions being edited after kickoff
                if fixture.is_locked():
                    continue

                # Retrieve the cleaned form data
                home = form.cleaned_data.get("predicted_home_goals")
                away = form.cleaned_data.get("predicted_away_goals")

                # Skip fixtures where the user left both fields blank
                if home is None and away is None:
                    continue

                # Save prediction
                prediction = form.save(commit=False)

                # Attach user and fixture before saving
                prediction.user = request.user
                prediction.fixture = fixture

                prediction.save()

            # Provide user feedback after saving predictions
            messages.success(request, "Matchweek predictions saved successfully.")

            # Redirect to avoid form resubmission if the page is refreshed
            return redirect("matchweek_predictions", matchweek=matchweek)

    else:

        # If GET request, display forms for each fixture
        for fixture in fixtures:

            existing_prediction = Prediction.objects.filter(
                user=request.user,
                fixture=fixture
            ).first()

            form = PredictionForm(
                instance=existing_prediction,
                prefix=f"fixture_{fixture.id}"
            )

            prediction_forms.append({
                "fixture": fixture,
                "form": form,
            })

    context = {
        "matchweek": matchweek,
        "prediction_forms": prediction_forms,
    }

    return render(
        request,
        "predictor/matchweek_predictions.html",
        context
    )