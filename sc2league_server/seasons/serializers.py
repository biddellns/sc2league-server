from rest_framework import serializers

from .models import Season, League

class LeagueSerializer(serializers.ModelSerializer):
    seasons = serializers.HyperlinkedRelatedField(
		many=True,
		read_only=True,
		view_name='season-detail')

    class Meta:
        model = League
        fields = ('id', 'name', 'seasons')

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ('league', 'uuid', 'season_number')
