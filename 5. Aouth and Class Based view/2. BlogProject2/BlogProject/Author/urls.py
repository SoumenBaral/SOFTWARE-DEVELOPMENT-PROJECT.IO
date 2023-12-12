from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.Register,name='register'),
    path('login/',views.LogIn,name='login'),
    path('logout',views.userLogOut,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('edit',views.EditProfile,name='edit_profile')

]
