from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # authentication & authorization routes
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    
    # product routes
    path("api/v1/", include('products.urls')),
    path("api/v1/", include('upload.urls')),
    
    # order routes
    path("api/v1/", include('orders.urls')),
]