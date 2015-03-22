from django.shortcuts import render
from screen.models import League,Team,Coach,Player
from rest_framework import viewsets
from screen.serializers import LeagueSerializer,TeamSerializer,CoachSerializer,PlayerSerializer


class LeagueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class CoachViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
