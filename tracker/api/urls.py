from django.conf.urls import url, include
from rest_framework import routers
from tracker.api import views

router = routers.DefaultRouter()
router.register(r'children', views.ChildViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/', views.login),
    url(r'^signup/', views.signup),
    #url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
