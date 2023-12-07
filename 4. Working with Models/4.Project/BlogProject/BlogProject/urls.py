
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('Posts/',include('Posts.urls')),
    path('author/',include('Author.urls')),
    path('Profiles/',include('Profiles.urls')),
    path('Categories/',include('Categories.urls')),
    path('',views.Home,name="home")
    
]
