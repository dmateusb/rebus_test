from django.db import models
from django.core.exceptions import ValidationError
from api.models.team import Team
from datetime import date


def validate_shirt_number(number):

    if number < 1 or number > 99:
        raise ValidationError("The shirt number must be between 1 and 99.")

class PlayerManager(models.Manager):
    
    def youngest_player(self, reverse=False):
        column = '-birthday' if reverse else 'birthday'
        try:
            return Player.objects.all().order_by(column)[0]
        except IndexError:
            return None

    def substitutes(self):
        return self.filter(is_titular=False)

    def players_age_mean(self):
        total_ages = 0
        for player in Player.objects.all(): total_ages += player.age()
        return total_ages / Player.objects.all().count()


class Player(models.Model):
    name = models.TextField(null=False, max_length=45)
    last_name = models.TextField(null=False, max_length=45)
    birthday = models.DateField(null=False)
    position = models.TextField(null=False, max_length=45)
    shirt_number = models.IntegerField(
        null=False, validators=[validate_shirt_number])
    is_titular = models.BooleanField(null=False)
    team = models.ForeignKey(to=Team, on_delete=models.CASCADE)
    objects = PlayerManager()
# photo

    def __str__(self):
        return "{} {}".format(self.name, self.last_name)

    def age(self):
        return date.today().year - self.birthday.year


    class Meta:
        app_label = 'api'
