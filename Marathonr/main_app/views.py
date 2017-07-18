""" Views file for main_app """
import json
import requests
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import Movie
from .marathons import Marathons
from .query import query_tmsapi
from .forms import LoginForm, SignUpForm, MarathonBasicsForm, MarathonMoviesForm

BASE_URL = 'http://data.tmsapi.com/v1.1/movies/showings'

#this will show index of user's marathons in future versions
def index(request):
    """function to show index of DB movies (for testing)"""
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})

def about(request):
    """function to show about page"""
    return render(request, 'about.html')

def home(request):
    """function to show home page"""
    return render(request, 'home.html')

#this will be rolled out in future versions
def show(request, movie_id):
    """function to show a single movie object"""
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'show.html', {'movie': movie})

def get_movies(request):
    """ Renders view with live movie data from ```query_tmsapi``` function """
    res = query_tmsapi(request, mfilter=True)
    return render(request, 'index.html', {'movies': res['movies']})

def signup(request):
    """function to signup new users"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form, 'message': 'Something went wrong...'})

def login_view(request):
    """function to render login form"""
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/home')
                else:
                    return render(request, 'login.html', {'form': form, 'message': "The account has been disabled."})
            else:
                return render(request, 'login.html', {'form': form, 'message': "The username and/or password is incorrect."})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    """function to call logout and redirect to homepage"""
    logout(request)
    return HttpResponseRedirect('/')

#this will be fully rolled out in future versions
def profile(request, username):
    """function to show profile page"""
    user = User.objects.get(username=username)
    movies = Movie.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'movies': movies})

def set_basics_form(request):
    """function to show form-one page"""
    form = MarathonBasicsForm()
    return render(request, 'form-one.html', {'form': form})

def set_movies_form(request):
    """function to show form-two page"""
    res = query_tmsapi(request, mfilter=False)
    return render(request, 'form-two.html', {'movies': res['movies'], 'zip': res['zip'], 'startDate': res['startDate']})

def get_marathons(request):
    """function to get marathons"""
    res = query_tmsapi(request, mfilter=True)
    marathons = Marathons(movies=res['movies'])
    return render(request, 'index.html', {'marathons': marathons})
