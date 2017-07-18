"""this is the forms file """
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Movie
from bootstrap3_datepicker.fields import DatePickerField
from bootstrap3_datepicker.widgets import DatePickerInput

# setting up the initial form for user to fill out
class MarathonBasicsForm(forms.Form):
    """ Step 1/first form for users to fill out """
    # TODO: Consider using a datepicker widget to make for easier and more consistent date selection.  Also is there logic to handle an accidental past date or future date too far ahead?
    startDate = forms.DateField(label='Date (YYYY-MM-DD)')
    zip = forms.CharField(label='ZIP (xxxxx)', max_length=5)

class MarathonMoviesForm(forms.Form):
    """ Step 2/second form for users to fill out """
    movie_one = forms.CharField(label='Movie 1', max_length=100)
    movie_two = forms.CharField(label='Movie 2', max_length=100)
    movie_three = forms.CharField(label='Movie 3', max_length=100)
    movie_four = forms.CharField(label='Movie 4', max_length=100)

class SignUpForm(UserCreationForm):
    """ Signup form for new users to fill out """
    # TODO: Consider adding an asterisk to the required field and not including the 'Optional' help text (clears up the view a bit)
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        """ Accessing the User model from Django """
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class LoginForm(forms.Form):
    """ Login form for users to sign in """
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
