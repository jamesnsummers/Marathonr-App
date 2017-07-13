"""Models file for main_app"""
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import re

class Movie(models.Model):
    """this is the Movie model"""
    tmsId = models.CharField(max_length=15, default='MV000000000000')
    title = models.CharField(max_length=50)
    run_time = models.CharField(max_length=10, default='PT00H00M')
    showtimes_raw = models.CharField(max_length=1000000, default='0')
    ratings_raw = models.CharField(max_length=1000, default='NR')
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title

    @property
    def run_minutes(self):
        """
        Takes dict `movie` with key `runTime` (str) and returns the runtime of the
        movie as a number of minutes (int).
        """
        runtime_format = r'PT([0-9]{2})H([0-9]{2})M'

        try:
            match = re.match(runtime_format, self.run_time)
            hours, mins = match.groups()
            return int(hours) * 60 + int(mins)

        except KeyError:
            return 'n/a'

    @property
    def showtimes(self):
        """ returns params of the showtimes that we'll need to use in the template """
        return [Showtime(movie=self,
                         start_time_raw=x['dateTime'],
                         theater_raw=x['theatre'],
                         ticketURI=x.get('ticketURI')) for x in self.showtimes_raw]

    @property
    def mpaa_rating(self):
        """ returns params of the ratings that we'll need to use in the template """
        for rating in self.ratings_raw:
            if rating['body'] == "Motion Picture Association of America":
                return rating['code']
                return 'NR'


class Showtime(models.Model):
    """
    this is the show time model
    We get something like this from the API:
        {u'barg': False,
         u'dateTime': u'2017-07-11T19:00',
         u'theatre': {u'id': u'9489', u'name': u'Alamo Drafthouse at the Ritz'},
         u'ticketURI': u'http://www.fandango.com/tms.asp?t=AAUQP&m=166105&d=2017-07-11'}
    """
    start_time_raw = models.CharField(max_length=16)
    theater_raw = models.CharField(max_length=50)
    ticketURI = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie)

    def __str__(self):
        return "{} @ {} {}".format(self.movie.title, self.theater, self.start_time)

    @property
    def start_time(self):
        """ formats the start time to be prettier for use in the template """
        return datetime.strptime(self.start_time_raw, '%Y-%m-%dT%H:%M')

    @property
    def theater(self):
        """ returns the theatre name for use in the template """
        return self.theater_raw['name']

    @property
    def end_time(self):
        """
        Takes datetime `start_time` and int `run_minutes` and returns
        a datetime for the end time of the movie.
        """
        return self.start_time + timedelta(0, self.movie.run_minutes * 60)
