"""views file for main_app"""
import json
import requests
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import Movie
from .query import query_tmsapi
from .forms import LoginForm, SignUpForm, MarathonForm

BASE_URL = 'http://data.tmsapi.com/v1.1/movies/showings'

def index(request):
    """function to show index of DB movies (for testing)"""
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})

def get_movies(request):
    """ Renders view with live movie data from ```query_tmsapi``` function """
    print("get_movies")
    movies = query_tmsapi(request)
    return render(request, 'index.html', {'movies': movies})

def show(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'show.html', {'movie': movie})

def profile(request, username):
    user = User.objects.get(username=username)
    movies = Movie.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'movies': movies})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user. is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def create(request):
    # if request.method == 'POST':
    #     form = MarathonForm(request.POST)
    #
    #     movies = query_tmsapi(request)
    #     return render(request, 'index.html', {'movies': movies})
    #
    #     # if form.is_valid():
    #     #     form.save()
    # else:
    form = MarathonForm()
    return render(request, 'form.html', {'form': form})

# def search(request):
#     movies = query_tmsapi(request)
#     return render(request, 'index.html', {'movies': movies})
