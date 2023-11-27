from django.urls import path
from . import views

urlpatterns = [
    path("course/", views.courses),
    path("about/", views.about),
    path("",views.home)


]