"""
URL configuration for SKP_DjangoWebApp project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("registration/", include("registration.urls")),
]
