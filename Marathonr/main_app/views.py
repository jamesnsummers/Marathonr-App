"""views file for main_app"""
from django.shortcuts import render

def index(request):
    """function to show index"""
    return render(request, 'index.html', {'movies': movies})

class Movie:
    def __init__(self, title, theatre, showtimes):
        self.title = title
        self.theatre = theatre
        self.showtimes = showtimes


movies = [
    Movie('Baby Driver', 'Alamo Drafthouse Mueller', '12:45pm, 3:30pm, 6:10pm, 7:30pm, 9:30pm, 10:35pm'),
    Movie('The Big Sick', 'Violet Crown Cinema', '11:00am, 1:45pm, 4:00pm, 6:30pm, 9:20pm, 10:45pm'),
    Movie('Wonder Woman', 'Alamo Drafthouse South Lamar', '' )
]
