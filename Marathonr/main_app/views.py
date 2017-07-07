"""views file for main_app"""
from django.shortcuts import render

def index(request):
    """function to show index"""
    return render(request, 'index.html')
