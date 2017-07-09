"""this is the forms file """
from django import forms
# setting up the initial form for user to fill out

class MarathonForm(forms.Form):
    date = forms.DateField(label='yyyy.mm.dd')
    zip_code = forms.PositiveIntegerField(label='ZIP', max_digits=7)
    distance_radius = forms.DecimalField(label='Value', max_digits=3, decimal_places=0)
    distance_units = forms.CharField(label='Material', max_length=100)
    movie_one = forms.CharField(label='movie_1', max_length=50)
    movie_two = forms.CharField(label='movie_2', max_length=50)
    movie_three = forms.CharField(label='movie_3', max_length=50)
    movie_four = forms.CharField(label='movie_4', max_length=50)
