"""admin file for main_app"""
from django.contrib import admin
from .marathons import Movie

admin.site.register(Movie)
