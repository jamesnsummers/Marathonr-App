"""views file for main_app"""
import json
import requests
from django.shortcuts import render
from .models import Movie

def index(request):
    """function to show index"""
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})

BASE_URL = 'http://data.tmsapi.com/v1.1/movies/showings'

def query_tmsapi(resource_url):
    url = '{0}{1}'.format(BASE_URL, resource_url)
    response = requests.get(url)

    if response.status_code == 200:
        return json.loads(response.text)
        # how do I return a render of the json data here?
    return None

film = query_tmsapi('?startDate=2017-07-07&zip=78701&api_key=t6ubhgkku8gu397wbnpjkb4j')

print(film[0])
