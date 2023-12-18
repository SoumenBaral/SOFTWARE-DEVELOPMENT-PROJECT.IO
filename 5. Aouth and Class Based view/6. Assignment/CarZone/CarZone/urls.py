from . import views
from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='home'),
    path('user/',include('UserAuth.urls')),
    path('brand/',include('carsBrand.urls')),
    path('car/',include('carModel.urls')),
    path('brand/<slug:brand_slug>/', views.Home, name='brand_wise'),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)