from django.urls import path, include
from rest_framework import routers
from tracker.api import views

router = routers.DefaultRouter()
router.register(r'children', views.ChildViewSet)
router.register(r'child_location', views.ChildLocationViewSet)
router.register(r'child_device', views.ChildDeviceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.login),
    path('signup/', views.signup),
]
