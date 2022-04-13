from django.db import models

class TeamManager(models.Manager):

    def biggest_team(self):
        biggest_team = None
        max_players_in_team = 0
        for team in Team.objects.all(): 
            team_size= team.players_count()
            if team_size > max_players_in_team:
                max_players_in_team = team_size
                biggest_team = team
        return biggest_team


    def substituded_players_mean(self):
        substituted_players = 0
        for team in Team.objects.all(): substituted_players += team.substitutes_count() 
        return substituted_players / Team.objects.all().count()


    def players_mean(self):
        total_players = 0
        for team in Team.objects.all(): total_players += team.player_set.count() 
        return total_players / Team.objects.all().count()

class Team(models.Model):
    name = models.TextField(null=False, max_length=45)
    flag = models.ImageField(upload_to='team-flags', null= True)
    shield = models.ImageField(upload_to='team-shields', null= True)
    objects = TeamManager()

    def __str__(self):
        return self.name

    def substitutes_count(self):
        return self.player_set.all().filter(is_titular=False).count()

    def players_count(self):
        return self.player_set.all().count()

    class Meta:
        app_label = 'api'
