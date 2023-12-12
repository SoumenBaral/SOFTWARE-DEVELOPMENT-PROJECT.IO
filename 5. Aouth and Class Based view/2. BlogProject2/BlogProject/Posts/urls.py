from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.AddPost,name="addPost"),
    path('edit/<int:id>',views.EditPost, name='edit'),
    path('delete/<int:id>',views.DeletePost, name='delete'),
]

