

from django.urls import path,include
from . import views

urlpatterns = [
   
    path('',views.Home,name='home'),
    path('signUp/',views.signUp,name='signUp')
]
