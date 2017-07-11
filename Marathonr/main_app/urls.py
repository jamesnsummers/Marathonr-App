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
    url(r'^about/$', views.about),
    url(r'^home/$', views.home),
    url(r'^form-one/$', views.set_basics_form, name="form-one"),
    url(r'^form-one/movies/$', views.set_movies_form),
    url(r'^form-one/form-two/$', views.set_movies_form, name="form-two"),
    url(r'^form-one/form-two/marathon/$', views.get_movies),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^$', index),
]
