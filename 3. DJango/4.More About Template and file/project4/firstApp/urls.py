

from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.AppHome ,name ="Home" ),
    path("about/<int:id>/", views.about, name="about")
]