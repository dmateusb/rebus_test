from django.urls import path, include
from services.views import ServicesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', ServicesViewSet, basename="services")


urlpatterns = [
  path('', include(router.urls)),
]
