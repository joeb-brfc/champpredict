from django.shortcuts import render, get_object_or_404
from .models import Fixture

# Create your views here.
def home(request):
    return render(request, "predictor/home.html")

def fixture_list(request):
    fixtures = Fixture.objects.all()

    context = {
        "fixtures": fixtures
    }

    return render(request, "predictor/fixture_list.html", context)


def fixture_detail(request, fixture_id):
    fixture = get_object_or_404(Fixture, id=fixture_id)

    context = {
        "fixture": fixture
    }

    return render(request, "predictor/fixture_detail.html", context)