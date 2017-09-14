from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

from sc2league_server.leagues.models import League

import uuid as uuid_lib

# Create your models here.
class Season(models.Model):
    league = models.ForeignKey(League, related_name="seasons", null=True) 
    season_number = models.IntegerField()
    uuid = models.UUIDField(
            db_index=True,
            default=uuid_lib.uuid4,
            editable=False)

    def __str__(self):
        return "Season #" + str(self.season_number)

    class Meta:
        unique_together = ("league", "season_number")
