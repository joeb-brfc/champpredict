from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class Fixture(models.Model):
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

    def __str__(self):
        return f"MW{self.matchweek} - {self.home_team} vs {self.away_team}"
