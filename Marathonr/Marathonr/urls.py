"""Marathonr URL Configuration"""
from django.conf.urls import url
from django.contrib import admin
from main_app import views

urlpatterns = [
    url(r'^admin', admin.site.urls),
    # url(r'^movies$', views.get_movies),
    url(r'^', views.index),
]
