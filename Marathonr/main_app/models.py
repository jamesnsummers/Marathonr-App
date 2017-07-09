"""Models file for main_app"""
from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    """this is the Movie model"""
    title = models.CharField(max_length=50)
    theatre = models.CharField(max_length=50)
    showtimes = models.CharField(max_length=50)
    ticketURI = models.CharField(max_length=100)
    ratings_code = models.CharField(max_length=10)
    user = models.ForeignKey(User)

def __str__(self):
    return self.title
