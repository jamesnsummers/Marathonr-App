"""views file for main_app"""
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """index function to show or GET all"""
    return HttpResponse('<h1>Hello Cinefiles!</h1>')
