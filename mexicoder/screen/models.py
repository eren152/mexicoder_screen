from django.db import models


class League(models.Model):
    league_name = models.CharField(max_length=200)


class Team(models.Model):
    league = models.ForeignKey(League)
    team_name = models.CharField(max_length=200)


class Coach(models.Model):
    team = models.ForeignKey(Team)
    coach_name = models.CharField(max_length=200)


class Player(models.Model):
    team = models.ForeignKey(Team)
    player_name = models.CharField(max_length=200)