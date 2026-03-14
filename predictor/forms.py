from django import forms
from .models import Prediction


class PredictionForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = ["predicted_home_goals", "predicted_away_goals"]
