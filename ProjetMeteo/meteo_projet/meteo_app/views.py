from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

import requests
from .models import Ville



# Create your views here.
@login_required
def index(request):



    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=fr&appid=0b525e25280d65fc37f0a0f7914643d3'

    villes = Ville.objects.all()

    meteo_data = []

    for ville in villes :

        url2 = requests.get(url.format(ville)).json()

        data = {

            'ville' : ville,
            'temperature' : url2['main']['temp'],
            'description' : url2['weather'][0]['description'],
            'icon' : url2['weather'][0]['icon'],
            'pays' : url2['sys']['country'] ,
            'humidite' : url2['main']['humidity'] ,
            'min' : url2['main']['temp_min'] ,
            'max' : url2['main']['temp_max'] ,
            'vent' : url2['wind']['speed'], 
        }

        meteo_data.append(data)
    

    context ={'meteo_data' : meteo_data}
    
    return render(request,'index.html',context)
    


def Inscription(request):

    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        mdp = request.POST.get('mdp')

        Nouv_Utilisateur = User.objects.create_user(nom,email,mdp)
        Nouv_Utilisateur.save()

        return redirect('Connexion')

    return render(request,'Inscription.html')

def Connexion(request):

    if request.method == 'POST':
        nom = request.POST.get('nom')
        mdp = request.POST.get('mdp')

        utilisateur = authenticate(request , username=nom, password=mdp)

        if utilisateur is not None:

            login(request,utilisateur)
            return redirect ('index')

        else : 
            return HttpResponse('Aucun Utilisateur enregistrée avec ces parametres')


    return render(request,'Connexion.html') 


def Deconnexion(request):
    logout(request)
    return redirect('Connexion')