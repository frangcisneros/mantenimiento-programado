from django.urls import path, include
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path("api/", include("mantenimiento.api_urls")),
]
