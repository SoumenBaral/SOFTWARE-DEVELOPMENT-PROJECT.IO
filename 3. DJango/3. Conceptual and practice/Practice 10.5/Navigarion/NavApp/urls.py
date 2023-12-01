
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.NavHome),
    path('contact/',views.contact),
    path('about/',views.about)
   
]
