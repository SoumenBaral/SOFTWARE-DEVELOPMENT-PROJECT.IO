
from django.urls import path
from . import views
urlpatterns = [
   path('', views.form,name="homepage"),
   path('delete/<int:roll>',views.delete_student name = "delete_student")
]