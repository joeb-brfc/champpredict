from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Fixture, Prediction
from .forms import PredictionForm
from django.contrib.auth.decorators import login_required

 
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

        # If the user has already predicted, calculate points if a result exists
        if prediction:
            user_points = prediction.calculate_points()

    # If the form is submitted
    if request.method == "POST" and not fixture.is_locked():
        # Create a blank prediction form
        form = PredictionForm(request.POST, instance=prediction)

        if form.is_valid():
            prediction = form.save(commit=False)

            # attach logged-in user
            prediction.user = request.user

            # attach fixture
            prediction.fixture = fixture

            prediction.save()
            return redirect("fixture_detail", fixture_id=fixture.id)

    else:
        # display blank form
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
    predictions = Prediction.objects.filter(user=request.user)

    context = {
        "predictions": predictions
    }

    return render(request, "predictor/my_predictions.html", context)