from django.contrib import admin
from .models import Fixture, Result, Team

# Register your models here.

admin.site.register(Team)
admin.site.register(Fixture)
admin.site.register(Result)