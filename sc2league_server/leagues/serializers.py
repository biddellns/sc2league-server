from rest_framework import serializers

from .models import League

class LeagueSerializer(serializers.ModelSerializer):
    seasons = serializers.HyperlinkedRelatedField(
		many=True,
		read_only=True,
		view_name='season-detail')

    abbreviation = serializers.CharField(min_length=3, max_length=7)

    class Meta:
        model = League
        fields = ('id', 'name', 'abbreviation', 'seasons')
