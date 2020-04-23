from django.contrib import admin
from django.urls import path, include
from tracker.api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tracker.api.urls')),
]
