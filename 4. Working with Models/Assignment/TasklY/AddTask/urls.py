from django.urls import path
from . import views
urlpatterns = [
    path('task/',views.AddTask,name='AddTask'),
    path('edit/<int:id>',views.EditTask, name='edit'),
    path('delete/<int:id>',views.DeleteTask, name='delete'),
]