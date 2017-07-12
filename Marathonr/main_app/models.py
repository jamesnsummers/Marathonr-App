"""Models file for main_app"""
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
import re

class Movie(models.Model):
    """this is the Movie model"""
    tmsId = models.CharField(max_length=15, default='MV000000000000')
    title = models.CharField(max_length=50)
    theatre = models.CharField(max_length=50)
    start_time = models.CharField(max_length=50)
    ticketURI = models.CharField(max_length=100)
    ratings_code = models.CharField(max_length=10)
    run_time = models.CharField(max_length=10, default='PT00H00M')
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
    def end_time(self):
        """
        Takes datetime `start_time` and int `run_minutes` and returns
        a datetime for the end time of the movie.
        """
        return self.start_time + timedelta(0, self.run_minutes * 60)
