#-*- coding: utf-8 -*-
from django.shortcuts import render
from team.models import Team, Division, Season

def teams(request):
    season = Season.objects.filter(current=True).get()
    teams = season.team_set.filter(name__startswith='SHC Aumont').all().order_by('division__standing').all()
    players = Team.objects.filter(id=teams[0].id).get().players.all().order_by('position__standing', 'lastname', 'firstname')
    return render(request, 'team/teams.html', {'teams':teams, 'my_team': teams[0], 'players': players})

def teams_team(request, id_team):
    season = Season.objects.filter(current=True).get()
    teams = season.team_set.filter(name__startswith='SHC Aumont').all().order_by('division__standing').all()
    players = Team.objects.filter(id=1).get().players.all().order_by('position__standing', 'lastname', 'firstname')
    my_team = Team.objects.filter(id=id_team).get()
    return render(request, 'team/teams.html', {'teams':teams, 'my_team': my_team, 'players': players})