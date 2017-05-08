from django.db import models
from django.contrib.auth.models import User


class Sport(models.Model):
    name = models.CharField(max_length=30)
    calories_coeff = models.FloatField()
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Activity(models.Model):
    SPORTS = [("Yoga", "Yoga"),
              ("Top Body Challenge", "Top Body Challenge"),
              ("Cours les Mills", "Cours les Mills"),
              ("Elliptique", "Elliptique"),
              ("Jogging", "Jogging")]
    sport = models.CharField(max_length=10, choices= SPORTS)
    newsport = models.ForeignKey(Sport, null=True) # if we decide to extract the list of sports from a Sport table later on
    durée = models.IntegerField()
    date = models.DateTimeField(auto_now_add=False, auto_now=False)
    user = models.ForeignKey(User, null = True)
    def __unicode__(self):
        return self.sport
    class Meta:
        ordering = ['date']


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    friendwith = models.ManyToManyField('self', related_name='friend_with', symmetrical=True)
    def __unicode__(self):
        return self.user.username
    class Meta:
        ordering = ['user__date__joined']

