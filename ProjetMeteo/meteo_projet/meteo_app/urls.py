from django.urls import path
from .views import index,Connexion,Inscription, Deconnexion

urlpatterns =[
    path('acceuil/',index, name="index"),
    path('inscription/',Inscription, name="Inscription"),
    path('connexion/',Connexion, name="Connexion"),
    path('deconnexion/',Deconnexion, name="Deconnexion")
]