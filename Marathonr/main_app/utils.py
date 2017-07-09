from datetime import timedelta
import re

def get_minutes(movie):
    """
    Takes dict `movie` with key `runTime` (str) and returns the runtime of the
    movie as a number of minutes (int).
    """
    runtime_format = r'PT([0-9]{2})H([0-9]{2})M'

    try:
        match = re.match(runtime_format, movie['runTime'])
        hours, mins = match.groups()
        return int(hours) * 60 + int(mins)

    except KeyError:
        return 'n/a'

def end_time(start_time, run_minutes, padding=0):
    """
    Takes datetime `start_time` and int `run_minutes` and returns
    a datetime for the end time of the movie.
    """
    return start_time + timedelta(0, run_minutes * 60 + padding)
