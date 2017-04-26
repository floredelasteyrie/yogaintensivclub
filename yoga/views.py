from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from .forms import *
from .models import *
import math


def deconnexion(request):
    logout(request)
    return render(request, "logout.html")


def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("/")
            else:
                error = True
    else:
        form = ConnexionForm()

    return render(request, "login.html", locals())



def home(request):
    if not request.user.is_authenticated:
        return redirect("/login")

    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            selectsport = form.cleaned_data['sport']
            selectdurée = form.cleaned_data['duree']
            selectdate = form.cleaned_data['date']
            activité = Activity()
            activité.sport = selectsport
            activité.durée = selectdurée
            activité.user = request.user
            activité.date = selectdate
            activité.save()
            envoi = True

            return redirect("/activity")

    else:
        form = ActivityForm()
    return render(request, "index.html", locals())


def activity(request):
    if not request.user.is_authenticated:
        return redirect("/login")

    activité = Activity.objects.all().order_by("-date")
    return render(request, "activity.html", {'activitées': activité})


def suppr_activity(request, ide):
    post = Activity.objects.get(id=ide)

    if request.user == post.user:
        post.delete()

    return redirect("/activity")


def leaderboard(request):
    if not request.user.is_authenticated:
        return redirect("/login")

    userlist = User.objects.all()
    tableau1 = []
    calories1 = []
    compteur1 = 1
    for utilisateur in userlist:
        activitylist1 = Activity.objects.filter(user=utilisateur, sport="Yoga")
        temps = 0
        for activitée in activitylist1:
            temps += activitée.durée
        binome1 = {'temps': temps, 'utilisateur': utilisateur, 'calories': math.floor(temps*4.9666666667)}
        tableau1.append(binome1)
        compteur1 += 1

    tableau2 = []
    compteur2 = 1
    for utilisateur in userlist:
        activitylist2 = Activity.objects.filter(user=utilisateur, sport="Top Body Challenge")
        temps = 0
        for activitée in activitylist2:
            temps += activitée.durée
        binome2 = {'temps': temps, 'utilisateur': utilisateur, 'calories': math.floor(temps*8.666666667)}
        tableau2.append(binome2)
        compteur2 += 1

    tableau3 = []
    compteur3 = 1
    for utilisateur in userlist:
        activitylist3 = Activity.objects.filter(user=utilisateur, sport="Cours les Mills")
        temps = 0
        for activitée in activitylist3:
            temps += activitée.durée
        binome3 = {'temps': temps, 'utilisateur': utilisateur, 'calories': math.floor(temps*8.666666667)}
        tableau3.append(binome3)
        compteur3 += 1

    tableau4 = []
    compteur4 = 1
    for utilisateur in userlist:
        activitylist4 = Activity.objects.filter(user=utilisateur, sport="Elliptique")
        temps = 0
        for activitée in activitylist4:
            temps += activitée.durée
        binome4 = {'temps': temps, 'utilisateur': utilisateur, 'calories': math.floor(temps*11.6666666667)}
        tableau4.append(binome4)
        compteur4 += 1

    tableau5 = []
    compteur5 = 1
    for utilisateur in userlist:
        activitylist5 = Activity.objects.filter(user=utilisateur, sport="Jogging")
        temps = 0
        for activitée in activitylist5:
            temps += activitée.durée
        binome5 = {'temps': temps, 'utilisateur': utilisateur, 'calories': math.floor(temps*12.4)}
        tableau5.append(binome5)
        compteur5 += 1

    tableau6 = []
    for utilisateur in userlist:
        activitylist6 = Activity.objects.filter(user=utilisateur)
        compteur6 = 0
        temps = 0
        for activitée in activitylist6:
            compteur6 += 1
            temps += activitée.durée
        binome6 = {'temps': temps, 'utilisateur': utilisateur, 'fois': compteur6}
        tableau6.append(binome6)

    tab_calories = []
    for utilisateur in userlist:
        cal_totales = 0
        for tab in tableau1:
            if tab['utilisateur'] == utilisateur:
                cal_totales += tab['calories']
        for tab in tableau2:
            if tab['utilisateur'] == utilisateur:
                cal_totales += tab['calories']
        for tab in tableau3:
            if tab['utilisateur'] == utilisateur:
                cal_totales += tab['calories']
        for tab in tableau4:
            if tab['utilisateur'] == utilisateur:
                cal_totales += tab['calories']
        for tab in tableau5:
            if tab['utilisateur'] == utilisateur:
                cal_totales += tab['calories']
                cal_totales = math.floor(cal_totales)
        cor_calories = {'utilisateur': utilisateur, 'calories': cal_totales}
        tab_calories.append(cor_calories)

    return render(request, "leaderboard.html", locals())


def previousweeks(request):
    if not request.user.is_authenticated:
        return redirect("/login")

    return render(request, "weekly.html")


def liens(request):

    return render(request, "liens.html")
