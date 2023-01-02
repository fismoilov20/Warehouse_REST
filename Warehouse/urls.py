"""Warehouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from app.views import *


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Warehouse Rest API",
      default_version='v1',
      description="Automatization for Warehouses",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact("Firdavsbek Ismoilov. <fismoilov20@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('get-token', obtain_auth_token),

    path('products', ProductsAPIView.as_view()),
    path('products/<int:pk>', ProductsAPIView.as_view()),
    path('users', UserAPIView.as_view()),
    path('warehouses', WarehouseAPIView.as_view()),
    path('clients', ClientAPIView.as_view()),

]
