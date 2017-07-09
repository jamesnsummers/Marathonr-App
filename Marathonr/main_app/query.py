# import requests
# import json
#
# BASE_URL = 'http://data.tmsapi.com/v1.1/movies/showings'
# API_KEY = 't6ubhgkku8gu397wbnpjkb4j'
#
# def query_tmsapi(request):
#     print("query_tmsapi")
#     params = {'api_key': API_KEY}
#
#     for param in 'startDate', 'zip':
#         if request.GET.get(param):
#             print("Got param {}: {}".format(param, request.GET[param]))
#             params[param] = request.GET[param]
#
#     response = requests.get(BASE_URL, params=params)
#
#     if response.status_code == 200:
#         print("got a thing")
# #        return render(request, 'index.html', {'movies':response.json()})
#         return response.json()
#         # how do I return a render of the json data here?
#
#     else:
#         print("i can't believe you've done this")
#         print("Reponse status: {} {}".format(response.status_code, response.reason))
#         print(response.text)
#         # import pdb; pdb.set_trace()
#         # response.raise_for_status()
#
#     return None
