from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Season, League
from .serializers import SeasonSerializer, LeagueSerializer
# Create your views here.

class LeagueViewSet(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

class SeasonViewSet(viewsets.ModelViewSet):
    serializer_class = SeasonSerializer
    

    def get_queryset(self):
        queryset = Season.objects.all()

        league_id = self.request.query_params.get('league', None)

        if league_id is not None:
            queryset = Season.objects.filter(league=league_id)
        else:
            queryset = Season.objects.all()

        return queryset
