"""admin file for main_app"""
from django.contrib import admin
from .models import Movie

admin.site.register(Movie)
