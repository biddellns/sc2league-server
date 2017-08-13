from rest_framework import serializers

from .models import Season

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ('uuid', 'season_number')
