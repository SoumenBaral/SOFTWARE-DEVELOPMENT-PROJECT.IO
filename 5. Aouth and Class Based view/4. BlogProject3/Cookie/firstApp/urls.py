from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.setCookie),
    path('get/',views.getCookies),
    path('del/',views.deleteCookies),

]
