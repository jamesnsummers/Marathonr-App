""" marathons object file """
from .models import Movie
from datetime import timedelta
import re


class Marathons(object):

    def __init__(self, movies):
        self.PADDING_TIME = 30
        self.movies = movies
        self.schedules = self.create_schedules()

    def earliest(self):
        """
        returns movies in a list of tuples sorted by start time [(tms1, 10:00am), (tms2, 10:30am)]
        """
        d = {movie: movie.start_time for movie in self.movies}
        return sorted(d.items(), key=lambda x: x[1])

    def build_lineup(self, starter):
        lineup = []
        movies_by_time = self.earliest()
        lineup.append(starter)

        while movies_by_time:
            movies_by_time = self.remove_duplicates(lineup[-1], movies_by_time)
            if movies_by_time:
                try:
                    lineup.append(self.late_enough(lineup[-1], movies_by_time)[0])
                except IndexError:
                    pass

        return lineup

    def remove_duplicates(self, movies, watched):
        unwatched = []

        for movie in movies:
            if movie.title != watched.title:
                unwatched.append(movie)

        return unwatched

    def late_enough(self, just_watched, movies):
        possible = []
        next_start = just_watched.end_time + timedelta(self.PADDING_TIME)

        for movie in movies:
            if movie.start_time >= next_start:
                possible.append(movie)

        return possible

    def create_schedules(self):
        schedules = []
        for movie in self.movies:
            schedules.append(self.build_lineup(starter=movie))

        return schedules
