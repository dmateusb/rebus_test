from api.models import *
from api.serializers import TeamSerializer
from rest_framework import viewsets

class TeamViewSet(viewsets.ModelViewSet):
    
    serializer_class = TeamSerializer
    queryset = Team.objects.all()