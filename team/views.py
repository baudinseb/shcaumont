#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.db.models import Q
from team.models import Team, Division, Season

def standings(request):
    season = Season.objects.filter(current=True).get()
    aumont_teams = season.team_set.filter(name__startswith='SHC Aumont').all()   
    id_division = aumont_teams[0].division.id
    teams = season.team_set.filter(division=id_division).extra(select={"points": "wins * 2 + draws"}).order_by('points').reverse().all()
    return render(request, 'team/standings.html', {'aumont_teams':aumont_teams, 'teams': teams, 'my_team': aumont_teams[0]})

def standings_team(request, id_team):
    season = Season.objects.filter(current=True).get()
    aumont_teams = season.team_set.filter(name__startswith='SHC Aumont').all()    
    my_team = Team.objects.filter(id=id_team).get()
    
    teams = season.team_set.filter(division=my_team.division.id).extra(select={"points": "wins * 2 + draws"}).order_by('points').reverse().all()
    return render(request, 'team/standings.html', {'aumont_teams':aumont_teams, 'teams': teams, 'my_team': my_team})

def teams(request):
    season = Season.objects.filter(current=True).get()
    teams = season.team_set.filter(name__startswith='SHC Aumont').all()
    return render(request, 'team/teams.html', {'teams':teams})