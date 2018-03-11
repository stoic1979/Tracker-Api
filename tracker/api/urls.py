from django.conf.urls import url, include
from rest_framework import routers
from tracker.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'children', views.ChildViewSet)
router.register(r'auth', views.ChildViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/', views.login),
    #url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
