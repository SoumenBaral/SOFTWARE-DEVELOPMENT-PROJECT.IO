from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.Register,name='register'),
    path('login/',views.LogIn,name='login'),
    path('logout',views.Register,name='logout')

]
