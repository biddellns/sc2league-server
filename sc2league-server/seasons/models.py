from django.db import models

import uuid as uuid_lib

# Create your models here.
class Season(models.Model):
    season_number = models.IntegerField()
    uuid = models.UUIDField(
            db_index=True,
            default=uuid_lib.uuid4,
            editable=False)

