from django.urls import path
from . import views
urlpatterns = [
    path('musician/',views.AddMusician.as_view() , name= 'addMus')
    

]