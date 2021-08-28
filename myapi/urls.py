from django.urls import include, path, re_path
from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter


router = routers.DefaultRouter()
router.register(r'maps', views.MapViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
  #  path('', include(router.urls)),
 #   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path('^', include(router.urls))
]