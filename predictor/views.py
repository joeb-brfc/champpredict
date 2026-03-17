from django.shortcuts import render, get_object_or_404, redirect
from .models import Fixture, Prediction
from .forms import PredictionForm


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
    # If the user is logged in, try to get their existing prediction for this fixture
    if request.user.is_authenticated:
        prediction = Prediction.objects.filter(
            user=request.user,
            fixture=fixture
        ).first()

    # If the form is submitted
    if request.method == "POST":
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
    }

    # Render the fixture detail page
    return render(request, "predictor/fixture_detail.html", context)