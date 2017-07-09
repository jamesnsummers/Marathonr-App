"""views file for main_app"""
import json
import requests
from django.shortcuts import render
from .models import Movie
# from .query import query_tmsapi

def index(request):
    """function to show index"""
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})

# BASE_URL = 'http://data.tmsapi.com/v1.1/movies/showings'
#
# def get_movies(request):
#     """ Renders view with live movie data from ```query_tmsapi``` function """
#     print("get_movies")
#     movies = query_tmsapi(request)
#     return render(request, 'index.html', {'movies': movies})
