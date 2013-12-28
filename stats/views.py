from django.shortcuts import render
from django.db import connection
from team.models import Season, Player
from stats.models import Stat

def team(request):
    season = Season.objects.filter(current=True).get()
    aumont_teams = season.team_set.filter(name__startswith='SHC Aumont').all()
    players_stats = stats_sql(aumont_teams[0].id)
    return render(request, 'stats/stats_team.html', {'aumont_teams': aumont_teams, 'my_team': aumont_teams[0], 'players_stats': players_stats })

def team_id(request, team_id):
    return render(request, 'stats/stats_team.html')



def stats_sql(team_id):
    cursor = connection.cursor()    
    cursor.execute("SELECT lastname, firstname, count(*) as games, sum(goals) as goals, sum(assists) as assists, sum(penalties) as penalties, sum(goals) + sum(assists) as points, schedule_schedule.game_type_id as type_game FROM team_player, stats_stat, schedule_schedule WHERE team_id = %s AND team_player.id = player_id AND schedule_schedule.id = calendar_id GROUP BY team_player.id, schedule_schedule.game_type_id ORDER BY type_game, points DESC", [team_id])
    return dictfetchall(cursor)


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]