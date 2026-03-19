from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# Team model
# Stores each Championship team once so the same team record can be reused across many fixtures.
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        # Teams will appear alphabetically by name
        ordering = ["name"]

    def __str__(self):
        # This is how the object will appear in admin and shell
        return self.name
    
    
# Fixture model
# Represents one scheduled match between two teams.
class Fixture(models.Model):

    # These choices control the available values for fixture status
    STATUS_CHOICES = [
        ("upcoming", "Upcoming"),
        ("played", "Played"),
    ]

    # Example: "2025/26"
    season = models.CharField(max_length=20)

    # Example: 1, 2, 3 etc
    matchweek = models.PositiveIntegerField()

    # The home team in the fixture
    home_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="home_fixtures"
    )

    # The away team in the fixture
    away_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="away_fixtures"
    )

    # Date and time the fixture kicks off
    kickoff_datetime = models.DateTimeField()

    # Current status of the fixture
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="upcoming"
    )

    class Meta:
        # Show fixtures in kickoff order
        ordering = ["kickoff_datetime"]

        # Prevent duplicate fixtures with the same season, matchweek,
        # home team and away team combination
        unique_together = ("season", "matchweek", "home_team", "away_team")

    def __str__(self):
        return f"MW{self.matchweek} - {self.home_team} vs {self.away_team}"

    def clean(self):
        # Prevent a team being selected as both home and away
        if self.home_team == self.away_team:
            raise ValidationError("A team cannot play itself.")

        # Look for other fixtures in the same season and matchweek
        # Exclude the current fixture so editing an existing record does not clash with itself
        existing_fixtures = Fixture.objects.filter(
            season=self.season,
            matchweek=self.matchweek
        ).exclude(pk=self.pk)

        # Check whether either selected team is already used in another fixture
        for fixture in existing_fixtures:
            if self.home_team in [fixture.home_team, fixture.away_team]:
                raise ValidationError(
                    f"{self.home_team} already has a fixture in matchweek {self.matchweek}."
                )

            if self.away_team in [fixture.home_team, fixture.away_team]:
                raise ValidationError(
                    f"{self.away_team} already has a fixture in matchweek {self.matchweek}."
                )
        
    def is_locked(self):
        # Returns True once kickoff time has passed
        # Used to stop predictions being edited after kickoff
        return timezone.now() >= self.kickoff_datetime

        
        
# Result model
# Stores the actual final score for a fixture.
class Result(models.Model):

    # One result per fixture
    fixture = models.OneToOneField(
        Fixture,
        on_delete=models.CASCADE,
        related_name="result"
    )

    # Actual goals scored by each team
    home_goals = models.PositiveIntegerField()
    away_goals = models.PositiveIntegerField()

    class Meta:
        # Show results in fixture kickoff order
        ordering = ["fixture__kickoff_datetime"]

    def __str__(self):
        return (
            f"{self.fixture.home_team} {self.home_goals} - "
            f"{self.away_goals} {self.fixture.away_team}"
        )


# Prediction model
# Stores one user's predicted score for one fixture.
class Prediction(models.Model):

    # The user who made the prediction
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # The fixture being predicted
    fixture = models.ForeignKey(
        Fixture,
        on_delete=models.CASCADE
    )

    # The user's predicted score
    predicted_home_goals = models.PositiveIntegerField()
    predicted_away_goals = models.PositiveIntegerField()

    # Automatically record when the prediction was created and updated
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Show predictions in fixture kickoff order
        ordering = ["fixture__kickoff_datetime"]

        # A user can only submit one prediction per fixture
        unique_together = ("user", "fixture")

    def __str__(self):
        return (
            f"{self.user.username} - "
            f"{self.fixture.home_team} {self.predicted_home_goals}:"
            f"{self.predicted_away_goals} {self.fixture.away_team}"
        )

    def clean(self):
        # Prevent predictions being created or changed after kickoff
            if self.fixture_id and self.fixture.is_locked():
                raise ValidationError(
                    "Predictions cannot be created or modified after kickoff."
                )

    def calculate_points(self):
        # If the fixture has no result yet, points cannot be calculated
        if not hasattr(self.fixture, "result"):
            return None

        # Actual result
        actual_home = self.fixture.result.home_goals
        actual_away = self.fixture.result.away_goals

        # User prediction
        predicted_home = self.predicted_home_goals
        predicted_away = self.predicted_away_goals

        # Exact score prediction = 3 points
        if predicted_home == actual_home and predicted_away == actual_away:
            return 3

        # Work out the match outcome from both actual and predicted scores
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

        # Correct result but wrong exact score = 1 point
        if actual_outcome == predicted_outcome:
            return 1

        # Incorrect result = 0 points
        return 0