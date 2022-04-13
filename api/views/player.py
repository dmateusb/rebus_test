from api.models import *
from api.serializers import PlayerSerializer
from rest_framework import viewsets

class PlayerViewSet(viewsets.ModelViewSet):
    
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()