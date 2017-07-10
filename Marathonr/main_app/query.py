import requests
import pickle
from datetime import datetime
# from dateutil import parser

BASE_URL = 'http://data.tmsapi.com/v1.1/movies/showings'
API_KEY = 't6ubhgkku8gu397wbnpjkb4j'
FAKE_DATA = True

def query_tmsapi(request):
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
        movies = response.json()

        for movie in movies:
            try:
                for showtime in movie['showtimes']:
                    show_date = datetime.strptime(showtime['dateTime'], '%Y-%m-%dT%H:%M')
                    showtime['dateTime'] = show_date.strftime('%H:%M')
            except KeyError as err:
                movie['theatre'] = {}
                movie['theatre']['showtimes'] = []
                movie['theatre']['name'] = 'FAKE THEATER'

        return movies

    else:
        print("Reponse status: {} {}".format(response.status_code, response.reason))
        print(response.text)
        import pdb; pdb.set_trace()
        response.raise_for_status()

    return None
