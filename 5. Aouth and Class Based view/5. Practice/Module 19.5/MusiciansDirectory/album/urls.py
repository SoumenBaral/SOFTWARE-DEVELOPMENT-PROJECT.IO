from django.urls import path
from . import views
urlpatterns = [
    path('album/',views.AddAlbum , name= 'addAlbum'),
    path('edit/<int:id>',views.EditAlbum, name='edit'),
    path('delete/<int:id>',views.DeletePost, name='delete'),
    path('login/',views.UserLoginView.as_view(), name ='login'),
    path('register/',views.RegistrationForms.as_view(),name='register'),
    path('logout/',views.logOut,name='logout')


]