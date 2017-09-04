from django.db import models

import uuid as uuid_lib

# Create your models here.

class League(models.Model):
    name = models.SlugField(max_length=75, unique=True)

    def __str__(self):
        return self.name

class Season(models.Model):
    league = models.ForeignKey('League', related_name="seasons", null=True) 
    season_number = models.IntegerField()
    uuid = models.UUIDField(
            db_index=True,
            default=uuid_lib.uuid4,
            editable=False)

    def __str__(self):
        return "Season #" + str(self.season_number)
