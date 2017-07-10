"""this is the forms file """
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Movie

# setting up the initial form for user to fill out
class MarathonForm(forms.Form):
    date = forms.DateField(label='yyyy-mm-dd')
    zip_code = forms.IntegerField(label='ZIP')
    distance_radius = forms.IntegerField(label='Search Radius')
    distance_units = forms.CharField(label='mi/km', max_length=100)
    movie_one = forms.ModelChoiceField(queryset=Movie.objects.all().order_by('title'))
    movie_two = forms.ModelChoiceField(queryset=Movie.objects.all().order_by('title'))
    movie_three = forms.ModelChoiceField(queryset=Movie.objects.all().order_by('title'))
    movie_four = forms.ModelChoiceField(queryset=Movie.objects.all().order_by('title'))

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
