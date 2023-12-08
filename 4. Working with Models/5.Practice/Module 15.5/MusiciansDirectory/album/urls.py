from django.urls import path
from . import views
urlpatterns = [
    path('album/',views.AddAlbum , name= 'addAlbum'),
    path('edit/<int:id>',views.EditAlbum, name='edit'),
    path('delete/<int:id>',views.DeletePost, name='delete'),

]