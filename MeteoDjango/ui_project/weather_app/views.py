from django.shortcuts import render,redirect
import requests
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session

from django.contrib.auth import authenticate, login, logout


# @login_required ( erreur django_session)
def weather(request):
    city = request.GET.get('city')
    context ={}
    if city:
        url = f'http://localhost:8000/weather_api/{city}'
        response = requests.get(url)
        if response.ok and response.content:
            data = response.json()
            context = {'data': data}
            return render(request, 'weather.html', context)
    return render(request, 'weather.html')


""" Modification du weather pour l'historique 
apres context = {'data' : data}

cities = request.COOKIES.get('cities', '')
            if city not in cities:
                cities += f'{city},'
            response = render(request, 'weather.html', context)
            response.set_cookie('cities', cities)
            return response
    # Récupérer l'historique des villes recherchées depuis le cookie
    cities = request.COOKIES.get('cities', '').split(',')
    context['cities'] = cities


"""


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        url = 'http://localhost:8000/login_api/'
        response = requests.post(url, {'username': username, 'password': password})

        if response.ok and response.content:
            data = response.json()
            if data['status'] == 'success':
                return redirect('weather')
            else:
                message = data['message']

    return render(request, 'login.html', {'message': message})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        url = 'http://localhost:8000/register_api/'
        response = requests.post(url, {'username': username, 'password1': password1, 'password2': password2, 'email': email})

        if response.ok and response.content:
            data = response.json()
            if data['status'] == 'success':
                messages.success(request, 'Inscription réussie. Vous pouvez maintenant vous connecter.')
                return redirect('login')
            else:
                messages.error(request, data['message'])
    else:
        messages.info(request, 'Veuillez remplir le formulaire ci-dessus pour vous inscrire.')
    return render(request, 'register.html')


def logout(request):
    url = 'http://localhost:8000/logout_api/'
    response = requests.post(url)
    if response.ok and response.content:
        data = response.json()
        if data['status'] == 'success':
            return redirect('login')
        else:
            message = data['message']
            
    return render(request, 'weather.html', {'message': message})
