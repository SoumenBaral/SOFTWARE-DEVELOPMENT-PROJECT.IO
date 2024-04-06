from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.setCookie),
    path('',views.setCookie),
    path('get/',views.getCookies),
    path('del/',views.deleteCookies),
    path('sets/',views.setSession),
    path('gets/',views.get_session),
    path('dels/',views.del_session),

]
