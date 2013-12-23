#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.db.models import Q
from team.models import Team, Division, Season

def standings(request):
    season = Season.objects.filter(current=True).get()
    teams = season.team_set.all()
    return render(request, 'team/standings.html', {'teams':teams})

def teams(request):
    season = Season.objects.filter(current=True).get()
    teams = season.team_set.filter(name__startswith='SHC Aumont')
    return render(request, 'team/teams.html', {'teams':teams})