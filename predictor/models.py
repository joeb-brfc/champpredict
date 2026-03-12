from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

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

    def __str__(self):
        return (
            f"{self.user.username} - "
            f"{self.predicted_home_goals}:{self.predicted_away_goals}"
        )