from django.contrib import admin
from .models import Fixture, Prediction, Result, Team

# Register your models here.

admin.site.register(Team)
admin.site.register(Fixture)
admin.site.register(Result)
admin.site.register(Prediction)