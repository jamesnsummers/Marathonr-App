"""views file for main_app"""
from django.shortcuts import render

def index(request):
    """function to show index"""
    return render(request, 'index.html', {'movies': movies})

class Movie:
    def __init__(self, title, theatre):
        self.title = title
        self.theatre = theatre


movies = [
    Movie('Baby Driver', 'Alamo Drafthouse Mueller'),
    Movie('The Big Sick', 'Violet Crown Cinema'),
    Movie('Wonder Woman', 'Alamo Drafthouse South Lamar')
]
