"""main_app URL Configuration"""
from django.conf.urls import url
from views import index
from views import show
from main_app import views
from .query import query_tmsapi

urlpatterns = [
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^([0-9]+)/$', show, name='show'),
    url(r'^movies/$', views.get_movies),
    url(r'^create/$', views.create, name="create"),
    url(r'^create/movies/$', views.get_movies, name="search"),
    url(r'^$', index),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
]
