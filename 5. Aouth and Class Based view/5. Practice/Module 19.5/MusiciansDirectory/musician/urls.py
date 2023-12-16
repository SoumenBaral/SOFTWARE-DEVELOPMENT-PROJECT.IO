from django.urls import path
from . import views
urlpatterns = [
    path('musician/',views.AddMusician.as_view() , name= 'addMus'),
    path('/editM/<int:id>/',views.EditMusicianView.as_view(), name='editM'),
]