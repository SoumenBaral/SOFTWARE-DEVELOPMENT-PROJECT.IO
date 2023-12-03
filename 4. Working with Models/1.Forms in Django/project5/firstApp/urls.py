from django.urls import path,include
from . import views
urlpatterns = [
    path('about/',views.About,name="About"),
    path('Form/',views.Form,name="Form")
]
