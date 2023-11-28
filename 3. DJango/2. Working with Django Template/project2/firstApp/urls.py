
from django.urls import path
# ----------------------------
# 3 ways to import views from app
# from firstApp.views import home
# from firstApp import views
# And finlay that is running under the line 
from . import  views
urlpatterns = [
  
    path('',views.home)
]