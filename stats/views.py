from django.shortcuts import render
from django.db import connection
from team.models import Season, Player, Team
from schedule.models import Type_Game
from stats.models import Stat

def team(request):
    season = Season.objects.filter(current=True).get()
    aumont_teams = season.team_set.filter(name__startswith='SHC Aumont').all()
    game_types = Type_Game.objects.all()
    players_stats = []
    
    for game_type in game_types:
        players_stats.append(stats_sql(aumont_teams[0].id, game_type.id))
        
    return render(request, 'stats/stats_team.html', {'aumont_teams': aumont_teams, 'my_team': aumont_teams[0], 'players_stats': players_stats })

def team_id(request, team_id):
    season = Season.objects.filter(current=True).get()
    aumont_teams = season.team_set.filter(name__startswith='SHC Aumont').all()
    my_team = Team.objects.filter(id=team_id).get()
    game_types = Type_Game.objects.all()
    players_stats = []
    
    for game_type in game_types:
        players_stats.append(stats_sql(team_id, game_type.id))
        
    return render(request, 'stats/stats_team.html', {'aumont_teams': aumont_teams, 'my_team': my_team, 'players_stats': players_stats })



def stats_sql(team_id, game_type_id):
    cursor = connection.cursor()    
    cursor.execute("SELECT lastname, firstname, type_name, count(*) as games, sum(goals) as goals, sum(assists) as assists, sum(penalties) as penalties, sum(goals) + sum(assists) as points FROM team_player, stats_stat, schedule_schedule, schedule_type_game WHERE team_id = %s AND game_type_id = %s AND team_player.id = player_id AND schedule_type_game.id = game_type_id AND schedule_schedule.id = calendar_id GROUP BY team_player.id ORDER BY points DESC", [team_id, game_type_id])
    return dictfetchall(cursor)


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]