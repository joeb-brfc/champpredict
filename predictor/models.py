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

    def __str__(self):
        return f"Matchweek {self.matchweek}"
