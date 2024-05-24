from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Ecommerce API",
      default_version='v1',
      description="API description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Admin site
    path("admin/", admin.site.urls),

    # authentication & authorization routes
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),

    # product routes
    path("api/v1/", include('products.urls')),
    path("api/v1/", include('upload.urls')),

    # order routes
    path("api/v1/", include('orders.urls')),

    # Swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Payment
    path('api/v1/payment/', include('paypal.standard.ipn.urls'))
]

urlpatterns += staticfiles_urlpatterns()
