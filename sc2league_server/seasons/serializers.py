from rest_framework import serializers

from .models import Season, League

class LeagueSerializer(serializers.ModelSerializer):
    seasons = serializers.StringRelatedField(many=True)

    class Meta:
        model = League
        fields = ('id', 'name', 'seasons',)

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ('league', 'uuid', 'season_number')
