from rest_framework import fields, serializers
from api.models import *

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["id", "name", "last_name","birthday","position","shirt_number","is_titular","team"]


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "name"]


class CouchingStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouchingStaff
        fields = ["id", "name", "last_name", "birthday", "birth_country", "rol", "team"]

