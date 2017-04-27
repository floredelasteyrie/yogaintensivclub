from django import forms
from . models import *
import datetime

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
	
class ActivityForm(forms.Form):
    SPORTS = [("Yoga","Yoga"),
              ("Top Body Challenge", "Top Body Challenge"),
              ("Cours les Mills", "Cours les Mills"),
              ("Elliptique", "Elliptique"),
              ("Jogging", "Jogging")]
    duree = forms.IntegerField()
    sport = forms.ChoiceField(choices=SPORTS)
    date = forms.DateTimeField(initial=datetime.date.today)

