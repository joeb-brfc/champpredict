from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("fixtures/", views.fixture_list, name="fixture_list"),
]