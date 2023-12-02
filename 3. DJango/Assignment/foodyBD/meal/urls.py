from django.urls import path
from . import views
urlpatterns = [
   
    path('',views.Meal,name="meal"),
]

