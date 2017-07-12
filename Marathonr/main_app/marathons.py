""" marathons object file """
from .models import Movie
from datetime import timedelta
import re


class Marathons(object):

    def __init__(self, movies):
        # Default to 30 minutes between movies
        self.PADDING_TIME = 30 * 60
        self.movies = movies
        self.showtimes = []

        for m in self.movies:
            self.showtimes.extend(m.showtimes)

        self.schedules = self.create_schedules()

        for x in self.schedules:
            print(x)

    def earliest(self):
        """
        returns movies in a list of tuples sorted by start time [(tms1, 10:00am), (tms2, 10:30am)]
        """
        return sorted(self.showtimes, key=lambda x: x.start_time)

    def build_lineup(self, starter_movie):
        i = 0
        lineup = []
        movies_by_time = self.earliest()

        # Get first showing of starter_movie
        for x in movies_by_time:
            if x.movie == starter_movie:
                starter_showtime = x
                break

        lineup.append(starter_showtime)
        print(starter_showtime.movie, starter_showtime)
        cutoff = len(movies_by_time)

        while movies_by_time:
            i += 1

            if i > cutoff:
                print("No options found.")
                break

            # remove last movie from movies_by_time until there are no more options
            movies_by_time = self.remove_duplicates(lineup[-1], movies_by_time)

            if movies_by_time:
                try:
                    lineup.append(self.late_enough(lineup[-1], movies_by_time)[0])
                except IndexError:
                    pass

        return lineup

    def remove_duplicates(self, ref, candidates):
        """ Takes Showtime object and returns candidate showtime list without it """
        unwatched = []

        for c in candidates:
            if ref.movie.title != c.movie.title:
                unwatched.append(c)

        return unwatched

    def late_enough(self, just_watched, candidates):
        """ Returns the first movie that starts late enough """
        possible = []
        next_start = just_watched.end_time + timedelta(0, self.PADDING_TIME)
        for showtime in candidates:
            if showtime.start_time >= next_start:
                possible.append(showtime)

        return possible

    def create_schedules(self):
        schedules = []

        for movie in self.movies:
            schedules.append(self.build_lineup(movie))

        return schedules
