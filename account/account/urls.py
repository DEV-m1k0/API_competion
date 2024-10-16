"""
URL configuration for account project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from drf_spectacular.views import SpectacularSwaggerView
from .views import *
from rest_framework.routers import DefaultRouter

pswd = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI4OTk1Mzg1LCJpYXQiOjE3Mjg5OTE3ODUsImp0aSI6IjAyNjg5OTg0MDFlZjRiZDM4ODM1MjBkYTExNzFkNjg3IiwidXNlcl9pZCI6MX0.V9ahTwgIVBu8dZcaN7J00yMHuwH8VbvQ-nJobQQ--qU"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/Accounts/Me', MyUserMeAPIView.as_view()), # Готов
    path('api/Accounts/Update', UpdateMeAPIView.as_view()), # Готов
    path('api/Accounts', MyUserAPI.as_view()),
    path('api/Accounts/<int:id>', MyUserByIdAPI.as_view()),
    path('api/Authentication/', include('api.urls')),
    path("api/Doctors", DoctorsAPIView.as_view()),
    path("api/Doctors/<int:id>", DoctorIdAPIView.as_view()),
    # Swagger UI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
