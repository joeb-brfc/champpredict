from django.db import models

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