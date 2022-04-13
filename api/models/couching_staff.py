from django.db import models
from django.core.exceptions import ValidationError
from api.models.team import Team


def validate_rol(rol):
    roles = ["tecnico", "asistente", "medico", "preparador"]
    if not rol in roles:
        raise ValidationError("The rol must be: {}.".format(", ".join(roles)))

class CouchingStaffManager(models.Manager):
    
    def technicians(self):
        return self.filter(rol='tecnico')

    def oldest_technician(self):
        try:
            return self.technicians().order_by('birthday')[0]
        except IndexError:
            return None
        

class CouchingStaff(models.Model):
    
    name = models.TextField(null=False, max_length=45)
    last_name = models.TextField(null=False, max_length=45)
    birthday = models.DateField(null=False)
    birth_country = models.TextField(null=False, max_length=45)
    rol = models.TextField(null=False, validators=[validate_rol])
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    objects = CouchingStaffManager()

    def __str__(self):
        return "{} {}".format(self.name, self.last_name)
# photo

    class Meta:
        app_label = 'api'

