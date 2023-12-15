
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.Home, name="home"),
    path('Posts/',include('Posts.urls')),
    path('author/',include('Author.urls')),
    path('Categories/',include('Categories.urls')),
    path('category/<slug:category_slug>/', views.Home, name='category_wise_post'),
   
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)