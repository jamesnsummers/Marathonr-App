import requests
import pickle
from datetime import datetime
from .models import Movie

BASE_URL = 'http://data.tmsapi.com/v1.1/movies/showings'
API_KEY = 't6ubhgkku8gu397wbnpjkb4j'
FAKE_DATA = True

def query_tmsapi(request, mfilter=False):
    """
    Uses GET params from request to query the API. Returns a dict of the
    JSON-encoded response.
    """

    print("query_tmsapi")
    params = {}

    expected = 'startDate', 'zip'

    for param in expected:
        if request.GET.get(param):
            print("Got param {}: {}".format(param, request.GET[param]))
            params[param] = request.GET[param]

    # Make sure we have a real query before we waste an API call
    if params:
        params['api_key'] = API_KEY

        try:
            fake_response = pickle.load(open('fakeresponse.pickle'))
        except:
            fake_response = None

        if not FAKE_DATA or not fake_response:
            "Real API request is happening!"
            response = requests.get(BASE_URL, params=params)
            pickle.dump(response, open('fakeresponse.pickle', 'w'))

        else:
            response = fake_response

        print("{}: {}".format(response.request.url, response.status_code))

    else:
        print("No query params passed to query_tmsapi")
        return {'hey':'whatup'}

    if response.ok:
        movies = []

        for m in response.json():
            try:
                vals = {'tmsId': m['tmsId'],
                        'title': m['title'],
                        'ratings_code': m['ratings'],
                        'run_time': m['runTime'],
                        'showtimes_raw': m['showtimes'],
                       }
                movie = Movie(**vals)
                movies.append(movie)

            except KeyError as err:
                print("Error loading key {} for {}".format(err, m.get('title')))

        if mfilter:
            return filter_movies(movies, request.GET)
        else:
            return {'movies': movies, 'zip': params['zip'], 'startDate': params['startDate']}

    else:
        print("Reponse status: {} {}".format(response.status_code, response.reason))
        print(response.text)

    return None

def filter_movies(movies, request):
    """function to filter through entire json response and return just titles"""
    titles = [k for k, v in request.iteritems() if v == 'on']
    return {'movies': [m for m in movies if m['title'] in titles]}
