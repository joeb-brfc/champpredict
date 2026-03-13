from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
    
    
class Fixture(models.Model):

    STATUS_CHOICES = [
        ("upcoming", "Upcoming"),
        ("played", "Played"),
    ]

    season = models.CharField(max_length=20)
    matchweek = models.PositiveIntegerField()

    home_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="home_fixtures"
    )

    away_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="away_fixtures"
    )

    kickoff_datetime = models.DateTimeField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="upcoming"
    )

    class Meta:
        ordering = ["kickoff_datetime"]
        unique_together = ("season", "matchweek", "home_team", "away_team")

    def __str__(self):
        return f"MW{self.matchweek} - {self.home_team} vs {self.away_team}"
    
    def clean(self):
        if self.home_team == self.away_team:
            raise ValidationError("A team cannot play itself.")
        
    def is_locked(self):
        return timezone.now() >= self.kickoff_datetime
        
        
class Result(models.Model):
    
    fixture = models.OneToOneField(
        Fixture,
        on_delete=models.CASCADE,
        related_name="result"
    )

    home_goals = models.PositiveIntegerField()
    away_goals = models.PositiveIntegerField()

    class Meta:
        ordering = ["fixture__kickoff_datetime"]

    def __str__(self):
        return (
            f"{self.fixture.home_team} {self.home_goals} - "
            f"{self.away_goals} {self.fixture.away_team}"
        )
    
class Prediction(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    fixture = models.ForeignKey(
        Fixture,
        on_delete=models.CASCADE
    )

    predicted_home_goals = models.PositiveIntegerField()
    predicted_away_goals = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["fixture__kickoff_datetime"]
        unique_together = ("user", "fixture")

    def __str__(self):
        return (
            f"{self.user.username} - "
            f"{self.fixture.home_team} {self.predicted_home_goals}:{self.predicted_away_goals} "
            f"{self.fixture.away_team}"
        )
    
    def clean(self):
        if self.fixture and self.fixture.is_locked():
            raise ValidationError(
                "Predictions cannot be created or modified after kickoff."
        )

    def calculate_points(self):
    # If the fixture has no result yet, we cannot calculate points
        if not hasattr(self.fixture, "result"):
            return None

        actual_home = self.fixture.result.home_goals
        actual_away = self.fixture.result.away_goals

        predicted_home = self.predicted_home_goals
        predicted_away = self.predicted_away_goals

    # Exact score = 3 points
        if predicted_home == actual_home and predicted_away == actual_away:
            return 3    
        
        actual_difference = actual_home - actual_away
        predicted_difference = predicted_home - predicted_away

        if actual_difference > 0:
            actual_outcome = "home_win"
        elif actual_difference < 0:
            actual_outcome = "away_win"
        else:
            actual_outcome = "draw"

        if predicted_difference > 0:
            predicted_outcome = "home_win"
        elif predicted_difference < 0:
            predicted_outcome = "away_win"
        else:
            predicted_outcome = "draw"

    # Correct outcome
        if actual_outcome == predicted_outcome:
            return 1

        return 0