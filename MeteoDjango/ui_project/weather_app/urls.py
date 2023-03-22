from django.urls import path
from .views import weather,login,register,logout

urlpatterns = [
    path('', weather, name='weather'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]
