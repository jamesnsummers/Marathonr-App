"""this is the forms file """
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Movie

# setting up the initial form for user to fill out
class MarathonBasicsForm(forms.Form):
    startDate = forms.DateField(label='Date (YYYY-MM-DD)')
    zip = forms.CharField(label='ZIP (xxxxx)', max_length=5)
    # distance_radius = forms.IntegerField(label='Search Radius')
    # distance_units = forms.ChoiceField(choices=[(' ', ' '), ('km', 'km'), ('mi', 'mi')])

class MarathonMoviesForm(forms.Form):
    movie_one = forms.CharField(label='Movie 1', max_length=100)
    movie_two = forms.CharField(label='Movie 2', max_length=100)
    movie_three = forms.CharField(label='Movie 3', max_length=100)
    movie_four = forms.CharField(label='Movie 4', max_length=100)

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
