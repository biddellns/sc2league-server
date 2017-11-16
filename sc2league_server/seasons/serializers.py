from rest_framework import serializers

from .models import Season, Round

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ('league', 'uuid', 'season_number')

class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = ('season', 'num_players_in', 'num_players_advancing', 'state')
