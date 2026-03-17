from django.contrib import admin
from .models import Team, Fixture, Result, Prediction


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    # Show team names in the admin list view
    list_display = ("name",)

    # Allow searching by team name
    search_fields = ("name",)


@admin.register(Fixture)
class FixtureAdmin(admin.ModelAdmin):
    # Show key fixture information in the list view
    list_display = ("home_team", "away_team", "season", "matchweek", "kickoff_datetime", "status")

    # Allow filtering fixtures by season, matchweek and status
    list_filter = ("season", "matchweek", "status")

    # Allow searching by team names
    search_fields = ("home_team__name", "away_team__name")

    # Display fixtures in kickoff order
    ordering = ("kickoff_datetime",)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    # Show result and related fixture in admin
    list_display = ("fixture", "home_goals", "away_goals")

    # Allow searching by fixture team names
    search_fields = ("fixture__home_team__name", "fixture__away_team__name")


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    # Show useful prediction details in admin
    list_display = (
        "user",
        "fixture",
        "predicted_home_goals",
        "predicted_away_goals",
        "created_at",
        "updated_at",
    )

    # Filter predictions by user and fixture
    list_filter = ("user", "fixture")

    # Allow searching by username and fixture team names
    search_fields = ("user__username", "fixture__home_team__name", "fixture__away_team__name")

    # Show predictions in fixture kickoff order
    ordering = ("fixture__kickoff_datetime",)  