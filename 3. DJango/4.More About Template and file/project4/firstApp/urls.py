

from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.AppHome ,name ="Home" ),
    path("about/", views.about, name="about")
]