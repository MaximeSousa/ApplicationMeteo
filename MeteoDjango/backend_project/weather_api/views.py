import requests
"""
from .models import Search
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from django.contrib.sessions.models import Session




@api_view(['GET'])
def weather_api(request, city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=fr&appid=0b525e25280d65fc37f0a0f7914643d3'
    response = requests.get(url)
    if response.ok and response.content:
        data = response.json()
        # Search.objects.create(city=city, user=request.user)
        return Response(data)
    else:
        return Response({'error': 'Une erreur s\'est produite lors de la récupération des données météorologiques.'})


"""
def search_history(request):
    searches = Search.objects.filter(user=request.user).order_by('-date')
    context = {'searches': searches}
    return render(request, 'search_history.html', context)

"""

@api_view(['POST'])
def login_api(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'status': 'success', 'message': 'Connexion réussie'})
    else:
        return Response({'status': 'error', 'message': 'Nom d\'utilisateur ou mot de passe incorrect'})


@api_view(['POST'])
def register_api(request):

    username = request.POST.get('username')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    email = request.POST.get('email')

    if username and password1 and password2 and email and password1 == password2:
        try:
            validate_password(password1)
        except ValidationError as e:
            return Response({'status': 'error', 'message': ', '.join(e)})
        
        user = User.objects.create_user(username=username, password=password1, email=email)
        user.save()
        
        if user:
            return Response({'status': 'success', 'message': 'Inscription réussie'})
    return Response({'status': 'error', 'message': 'Une erreur s\'est produite lors de l\'inscription,  vérifié bien que le mot de passe contient bien au moins 8 caracteres, minuscule, majuscule et caracteres spéciaux '})


@api_view(['POST'])
def logout_api(request):
    logout(request)
    return Response({'status': 'success', 'message': 'Déconnexion réussie'})