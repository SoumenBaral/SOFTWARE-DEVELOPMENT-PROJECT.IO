from django.urls import path
from . import views

urlpatterns = [
    path('album/',views.AddAlbum.as_view(), name= 'addAlbum'),
    path('edit/<int:id>',views.EditPostView.as_view(), name='edit'),
    path('delete/<int:id>',views.DeletePostView.as_view(), name='delete'),
    path('login/',views.UserLoginView.as_view(), name ='login'),
    path('register/',views.RegistrationForms.as_view(),name='register'),
    path('logout/',views.UserLogoutViewClass.as_view(),name='logout')


]