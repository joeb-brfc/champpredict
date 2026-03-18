from django.urls import path
from . import views

# URL routes for the predictor application
urlpatterns = [
    path("", views.home, name="home"),
    path("fixtures/", views.fixture_list, name="fixture_list"),
    path("fixture/<int:fixture_id>/", views.fixture_detail, name="fixture_detail"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
    path("my-predictions/", views.my_predictions, name="my_predictions"),

    # Bulk prediction page for a full Championship matchweek
    path(
        "matchweek/<int:matchweek>/",
        views.matchweek_predictions,
        name="matchweek_predictions"
    ),
]