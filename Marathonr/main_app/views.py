"""views file for main_app"""
from django.shortcuts import render
from .models import Movie

def index(request):
    """function to show index"""
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})
