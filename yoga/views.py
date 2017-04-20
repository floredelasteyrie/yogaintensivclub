from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from .forms import *
from .models import *

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
            else:  # sinon une erreur sera affichée
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
            activity = Activity()
            activity.sport = selectsport
            activity.durée = selectdurée
            activity.user = request.user
            activity.save()
		
            envoi = True

            return redirect("/activity")

    else:
        form = ActivityForm()
    return render(request, "index.html", locals())
	
def activity(request):
    if not request.user.is_authenticated:
        return redirect("/login")

    activity = Activity.objects.all()
    return render(request, "activity.html", {'activitées' :activity})

def suppr_activity(request,id):



    post = Activity.objects.get(id=id)

    if request.user == post.user:
        post.delete()

    return redirect("/activity")
	
def leaderboard(request):
    if not request.user.is_authenticated:
        return redirect("/login")

    return render(request, "leaderboard.html")
	
def previousweeks(request):
    if not request.user.is_authenticated:
        return redirect("/login")

    return render(request, "weekly.html")

def liens(request):

    return render(request, "liens.html")
	