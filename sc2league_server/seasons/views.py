from django.shortcuts import render

from rest_framework import viewsets

from .models import Season
from .serializers import SeasonSerializer
# Create your views here.

class SeasonViewSet(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
