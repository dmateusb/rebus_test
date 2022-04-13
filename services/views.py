from sqlalchemy import column, null
from api.serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from api.models import *
from rest_framework.decorators import action
from rest_framework import status

class ServicesViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['get'])
    def count_teams(self, request):
        result = Team.objects.count()
        return Response({ "result": result}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def count_players(self, request):
        result = Player.objects.count()
        return Response({ "result": result}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def youngest_player(self, request):
        result = Player.objects.youngest_player(True)
        if not result:
            return Response({"result": "Empty table"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = PlayerSerializer(result, many = False)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def oldest_player(self, request):
        result = Player.objects.youngest_player()
        if not result:
            return Response({"result": "Empty table"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = PlayerSerializer(result, many = False)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def substitute_players_count(self, request):
        result = Player.objects.substitutes().count()
        return Response({"result": result}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def substitute_players_mean(self, request):
        mean = Team.objects.substituded_players_mean()
        return Response({"result": mean}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def biggest_team(self, request):
        biggest_team = Team.objects.biggest_team()
        serializer = TeamSerializer(biggest_team)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def players_age_mean(self, request):
        players_age_mean = Player.objects.players_age_mean()
        return Response({"result": players_age_mean}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def team_players_mean(self, request):
        mean = Team.objects.players_mean()
        return Response({"result": mean}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def oldest_technician(self, request):
        result = CouchingStaff.objects.oldest_technician()
        if not result:
            return Response({"result": "Empty table"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = CouchingStaffSerializer(result, many = False)
            return Response(serializer.data, status=status.HTTP_200_OK)

    
