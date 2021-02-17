from django.db import models

from django.core.validators import MinLengthValidator

class League(models.Model):
    name = models.CharField(max_length=75, unique=True)
    abbreviation = models.CharField(max_length=7, unique=True, validators=[MinLengthValidator(3)])

    def __str__(self):
        return self.name
