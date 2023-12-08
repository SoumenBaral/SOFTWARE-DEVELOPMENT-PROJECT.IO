from django.urls import path
from . import views
urlpatterns = [
    path('album/',views.AddAlbum , name= 'addAlbum')

]