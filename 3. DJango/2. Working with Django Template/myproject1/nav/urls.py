from django.urls import path
from . import views

urlpatterns = [
    path ('', views.navHome),
    path('about/',views.about),
    path('contact/', views.contact),
    path('blog/',views.blog),

]
