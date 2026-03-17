from django.contrib import admin
from .models import Team, Fixture, Result, Prediction


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Fixture)
class FixtureAdmin(admin.ModelAdmin):
    list_display = ("home_team", "away_team", "matchweek", "kickoff_datetime")
    list_filter = ("matchweek",)
    search_fields = ("home_team__name", "away_team__name")
    ordering = ("kickoff_datetime",)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("fixture", "home_goals", "away_goals")


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ("user", "fixture", "predicted_home_goals", "predicted_away_goals")
    list_filter = ("fixture", "user")