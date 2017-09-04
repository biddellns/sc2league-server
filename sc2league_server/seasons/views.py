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
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    
    def list(self, request):
        queryset = Season.objects.all()

        league_id = request.query_params.get('league', None)

        if league_id is not None:
            queryset = Season.objects.filter(league=league_id)

        serializer = SeasonSerializer(queryset, many=True)
        return Response(serializer.data)
