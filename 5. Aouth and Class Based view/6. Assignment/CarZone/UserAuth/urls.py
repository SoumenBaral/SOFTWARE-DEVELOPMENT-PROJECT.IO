from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.RegistrationForms.as_view(),name='register'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('logout/',views.logOut.as_view(),name='logout'),
    path('update/',views.updateUserView.as_view(),name='update'),
    path('password/',views.PassWordChange.as_view(),name='password'),

    


]
