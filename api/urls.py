from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'players', PlayerViewSet)

urlpatterns = [
  path('', include(router.urls)),
  #path('teams', TeamListApiView.as_view()),
  #path('teams/<int:team_id>/', TeamDetailApiView.as_view()),
  path('couching_staffs', CouchingStaffListApiView.as_view()),
  path('couching_staffs/<int:couch_id>/', CouchingStaffDetailApiView.as_view()),
]
