from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.RegistrationForms.as_view(),name='register'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logOut.as_view(),name='logout')

]
