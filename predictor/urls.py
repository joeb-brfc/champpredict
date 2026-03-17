from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("fixtures/", views.fixture_list, name="fixture_list"),
    path("fixtures/<int:fixture_id>/", views.fixture_detail, name="fixture_detail"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
    path("my-predictions/", views.my_predictions, name="my_predictions"),
]