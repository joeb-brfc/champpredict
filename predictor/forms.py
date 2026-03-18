from django import forms
from .models import Prediction


class PredictionForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = ["predicted_home_goals", "predicted_away_goals"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Allow empty predictions when using bulk entry
        # This enables users to leave fixtures blank when submitting
        # predictions for an entire matchweek at once.
        self.fields["predicted_home_goals"].required = False
        self.fields["predicted_away_goals"].required = False

    # Custom validation based on Django ModelForm validation patterns
    # Reference: https://docs.djangoproject.com/en/stable/ref/forms/validation/
    # Ensures users cannot enter only one score (e.g. "2 -" or "- 1")
    def clean(self):
        cleaned_data = super().clean()
        home = cleaned_data.get("predicted_home_goals")
        away = cleaned_data.get("predicted_away_goals")

        # Ensure both scores are entered together
        if (home is None and away is not None) or (home is not None and away is None):
            raise forms.ValidationError(
                "Please enter both home and away goals."
            )

        return cleaned_data