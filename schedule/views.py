from django.shortcuts import render
from django.db.models import Q
from schedule.models import Schedule, Round, Type_Game
from team.models import Team, Division, Season


def regular(request):
    season = Season.objects.filter(current=True).get()
    aumont_teams = season.team_set.filter(name__startswith='SHC Aumont').all()
    id_division = aumont_teams[0].division.id
    teams = season.team_set.filter(division=id_division).extra(select={"points": "wins * 2 + draws"}).order_by('points').reverse().all()
    type_game = Type_Game.objects.filter(type_name='Championnat').get()
    games = Schedule.objects.filter(Q(game_type=type_game.id) & (Q(team_home=aumont_teams[0].id) | Q(team_away=aumont_teams[0].id))).order_by('date').all()
    return render(request, 'schedule/regular.html', {'aumont_teams': aumont_teams, 'my_team': aumont_teams[0], 'games': games, 'teams': teams})

def regular_team(request, id_team):
    season = Season.objects.filter(current=True).get()
    aumont_teams = season.team_set.filter(name__startswith='SHC Aumont').all()
    my_team = Team.objects.filter(id=id_team).get()
    teams = season.team_set.filter(division=my_team.division.id).extra(select={"points": "wins * 2 + draws"}).order_by('points').reverse().all()
    type_game = Type_Game.objects.filter(type_name='Championnat').get()
    games = Schedule.objects.filter(Q(game_type=type_game.id) & (Q(team_home=id_team) | Q(team_away=id_team))).order_by('date').all()
    return render(request, 'schedule/regular.html', {'aumont_teams': aumont_teams, 'my_team': my_team, 'games': games, 'teams': teams})

def cup(request):
    season = Season.objects.filter(current=True).get()
    aumont_teams = season.team_set.filter(name__startswith='SHC Aumont').all()   
    type_game = Type_Game.objects.filter(type_name='Regular').get()
    games = Schedule.objects.filter(Q(game_type=type_game) & (Q(team_home=aumont_teams[0].id) | Q(team_away=aumont_teams[0].id))).all()
    return render(request, 'team/standings.html', {'games': games})

def cup_team(request):
    season = Season.objects.filter(current=True).get()
    aumont_teams = season.team_set.filter(name__startswith='SHC Aumont').all()   
    type_game = Type_Game.objects.filter(type_name='Regular').get()
    games = Schedule.objects.filter(Q(game_type=type_game) & (Q(team_home=aumont_teams[0].id) | Q(team_away=aumont_teams[0].id))).all()
    return render(request, 'team/standings.html', {'games': games})

def playoffs(request):
    season = Season.objects.filter(current=True).get()
    aumont_teams = season.team_set.filter(name__startswith='SHC Aumont').all()   
    type_game = Type_Game.objects.filter(type_name='Regular').get()
    games = Schedule.objects.filter(Q(game_type=type_game) & (Q(team_home=aumont_teams[0].id) | Q(team_away=aumont_teams[0].id))).all()
    return render(request, 'team/standings.html', {'games': games})

def playoffs_team(request):
    season = Season.objects.filter(current=True).get()
    aumont_teams = season.team_set.filter(name__startswith='SHC Aumont').all()   
    type_game = Type_Game.objects.filter(type_name='Regular').get()
    games = Schedule.objects.filter(Q(game_type=type_game) & (Q(team_home=aumont_teams[0].id) | Q(team_away=aumont_teams[0].id))).all()
    return render(request, 'team/standings.html', {'games': games})
