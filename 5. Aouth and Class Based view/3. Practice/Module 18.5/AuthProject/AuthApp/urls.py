from django.urls import path 
from . import views


urlpatterns = [
    path('',views.Home, name='home'),
    path('register/',views.registered,name='register'),
    path('login/',views.logIn,name='login'),
    path('profile/',views.Profile,name='profile'),
    path('logout/',views.Logout,name='logout'),
    path('profile/',views.Profile,name='profile')
]
