
from django.contrib import admin
from django.urls import path,include
from .views import contact,home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
    path("firstApp/",include("firstApp.urls")),
    path('contact/',contact),
]
