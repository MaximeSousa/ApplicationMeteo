from django.urls import path
from .views import weather_api,login_api,register_api,logout_api

urlpatterns = [
    path('weather_api/<str:city>', weather_api, name='weather_api'),
    path('login_api/', login_api, name='login_api'),
    path('register_api/', register_api, name='register_api'),
    path('logout_api/', logout_api, name='logout_api'),
]