from django.urls import path
from . import views
urlpatterns = [
    path('djFrom/',views.DjangoForm, name="djFrom"),
    path('mForm/',views.DjangoModel,name='mForm')
]