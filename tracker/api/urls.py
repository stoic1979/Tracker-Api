from django.conf.urls import url, include
from rest_framework import routers
from tracker.api import views

router = routers.DefaultRouter()
# router.register(r'signup', views.UserCreate)
router.register(r'groups', views.GroupViewSet)
router.register(r'children', views.ChildViewSet)
router.register(r'auth', views.ChildViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/', views.login),
    url(r'^signup/', views.UserCreate.as_view(), name='account-create'),
    #url(r'^$', views.UserCreate.as_view(), name='account-create'),
    #url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
