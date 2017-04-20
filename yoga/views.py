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

    activity = Activity.objects.all().order_by("-date")
    return render(request, "activity.html", {'activitées' :activity})

def suppr_activity(request,id):



    post = Activity.objects.get(id=id)

    if request.user == post.user:
        post.delete()

    return redirect("/activity")
	
def leaderboard(request):
    if not request.user.is_authenticated:
        return redirect("/login")

    userlist1 = User.objects.all()
    tableau1 = []
    compteur1 = 1
    for utilisateur in userlist1:
        activitylist1 = Activity.objects.filter(user=utilisateur,sport="Yoga")
        temps = 0
        for activitée in activitylist1:
            temps += activitée.durée
            print(temps)
        binome1 = {'temps': temps, 'utilisateur': utilisateur}
        tableau1.append(binome1)
        compteur1 += 1

    userlist2 = User.objects.all()
    tableau2 = []
    compteur2 = 1
    for utilisateur in userlist2:
        activitylist2 = Activity.objects.filter(user=utilisateur,sport="Top Body Challenge")
        temps = 0
        for activitée in activitylist2:
            temps += activitée.durée
        binome2 = {'temps': temps, 'utilisateur': utilisateur}
        tableau2.append(binome2)
        compteur2 += 1

    userlist3 = User.objects.all()
    tableau3 = []
    compteur3 = 1
    for utilisateur in userlist3:
        activitylist3 = Activity.objects.filter(user=utilisateur,sport="Cours les Mills")
        temps = 0
        for activitée in activitylist3:
            temps += activitée.durée
        binome3 = {'temps': temps, 'utilisateur': utilisateur}
        tableau3.append(binome3)
        compteur3 += 1

    userlist4 = User.objects.all()
    tableau4 = []
    compteur4 = 1
    for utilisateur in userlist4:
        activitylist4 = Activity.objects.filter(user=utilisateur,sport="Elliptique")
        temps = 0
        for activitée in activitylist4:
            temps += activitée.durée
        binome4 = {'temps': temps, 'utilisateur': utilisateur}
        tableau4.append(binome4)
        compteur4 += 1


    userlist5 = User.objects.all()
    tableau5 = []
    compteur5 = 1
    for utilisateur in userlist5:
        activitylist5 = Activity.objects.filter(user=utilisateur,sport="Jogging")
        temps = 0
        for activitée in activitylist5:
            temps += activitée.durée
        binome5 = {'temps': temps, 'utilisateur': utilisateur}
        tableau5.append(binome5)
        compteur5 += 1

    return render(request, "leaderboard.html",locals())
	
def previousweeks(request):
    if not request.user.is_authenticated:
        return redirect("/login")

    return render(request, "weekly.html")

def liens(request):

    return render(request, "liens.html")
	