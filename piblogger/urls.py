"""
URL configuration for piblogger project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # URL patterns for users and pibloggers apps
    path('users/', include('users.urls')),
    path('', include('pibloggers.urls')),
]
