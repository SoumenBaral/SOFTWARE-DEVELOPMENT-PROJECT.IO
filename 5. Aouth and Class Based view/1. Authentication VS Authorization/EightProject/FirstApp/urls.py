

from django.urls import path,include
from . import views

urlpatterns = [
   
    path('',views.Home,name='home'),
    path('signUp/',views.signUp,name='signUp'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.LogOut,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('passWordChangeWithOld/',views.PassChangeWithOldPass,name='withOldPass'),
    path('passWordChangeWithOutOld/',views.PassChangeWithoutOldPass,name='withOutOldPass'),

    

]
