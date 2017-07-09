"""this is the forms file """
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# setting up the initial form for user to fill out

class MarathonForm(forms.Form):
    date = forms.DateField(label='yyyy.mm.dd')
    zip_code = forms.DecimalField(label='ZIP', max_digits=7)
    distance_radius = forms.DecimalField(label='Value', max_digits=3, decimal_places=0)
    distance_units = forms.CharField(label='Material', max_length=100)
    movie_one = forms.CharField(label='movie_1', max_length=50)
    movie_two = forms.CharField(label='movie_2', max_length=50)
    movie_three = forms.CharField(label='movie_3', max_length=50)
    movie_four = forms.CharField(label='movie_4', max_length=50)

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
