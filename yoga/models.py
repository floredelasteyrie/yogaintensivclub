from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    SPORTS = [("Yoga", "Yoga"),
              ("Top Body Challenge", "Top Body Challenge"),
              ("Cours les Mills", "Cours les Mills"),
              ("Elliptique", "Elliptique"),
              ("Jogging", "Jogging")]
    sport = models.CharField(max_length=10, choices= SPORTS)
    durée = models.IntegerField()
    date = models.DateTimeField(auto_now_add=False, auto_now=False)
    user = models.ForeignKey(User, null = True)
