
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='home'),
    path('add/',include('AddCategory.urls')),
    path('add/',include('AddTask.urls'))


]
