from django.shortcuts import render
from django.db import connection
from team.models import Season, Player, Team, Division
from schedule.models import Type_Game
from stats.models import Stat

def team(request):
    season = Season.objects.filter(current=True).get()
    aumont_teams = season.team_set.filter(name__startswith='SHC Aumont').all().order_by('division__standing').all()
    game_types = Type_Game.objects.all()
    all_stats = []
    
    for game_type in game_types:
        players_stats = stats_sql(aumont_teams[0].id, game_type.id)
        for player_stats in players_stats:
            player_stats['points_per_game'] = float(player_stats['points']) / float(player_stats['games'])
        all_stats.append(players_stats)
        
    return render(request, 'stats/stats_team.html', {'aumont_teams': aumont_teams, 'my_team': aumont_teams[0], 'players_stats': all_stats })

def team_id(request, team_id):
    season = Season.objects.filter(current=True).get()
    aumont_teams = season.team_set.filter(name__startswith='SHC Aumont').all().order_by('division__standing').all()
    my_team = Team.objects.filter(id=team_id).get()
    game_types = Type_Game.objects.all()
    all_stats = []
    
    for game_type in game_types:
        players_stats = stats_sql(team_id, game_type.id)
        for player_stats in players_stats:
            player_stats['points_per_game'] = float(player_stats['points']) / float(player_stats['games'])
        all_stats.append(players_stats)
        
    return render(request, 'stats/stats_team.html', {'aumont_teams': aumont_teams, 'my_team': my_team, 'players_stats': all_stats })

def player_id(request, player_id):
    player = Player.objects.filter(id=player_id).get()
    all_divisons = Division.objects.all()
    game_types = Type_Game.objects.exclude(type_name__startswith='Coupe').all()
    
    last_five_stats = Stat.objects.filter(player=player_id).all().extra(select={"points": "goals + assists"}).order_by('calendar__game_date').reverse()[:5]
    
    stats = []
    
    for division in all_divisons:
        stat_division = []
    
        for game_type in game_types:
            stat_division.append(player_stats_sql(player_id, division.id, game_type.id))
            
        stats.append(stat_division)
    
    return render(request, 'stats/stats_player.html', {'player': player, 'stats': stats, 'last_five': last_five_stats})

def record_player_id(request, player_id):
    player = Player.objects.filter(id=player_id).get()
    goals = Stat.objects.filter(player=player_id).extra(select={"points": "goals + assists"}).order_by('goals').reverse().all()[:5]
    assists = Stat.objects.filter(player=player_id).extra(select={"points": "goals + assists"}).order_by('assists').reverse().all()[:5]
    penalties = Stat.objects.filter(player=player_id).extra(select={"points": "goals + assists"}).order_by('penalties').reverse().all()[:5]
    points = Stat.objects.filter(player=player_id).extra(select={"points": "goals + assists"}).order_by('points').reverse().all()[:5]
    return render(request, 'stats/record_player.html', {'player': player, 'goals': goals, 'assists': assists, 'points': points, 'penalties': penalties})

def stats_sql(team_id, game_type_id):
    cursor = connection.cursor()    
    cursor.execute("SELECT lastname, firstname, type_name, count(*) as games, sum(goals) as goals, sum(assists) as assists, sum(penalties) as penalties, sum(goals) + sum(assists) as points FROM team_player, stats_stat, schedule_schedule, schedule_type_game WHERE team_id = %s AND game_type_id = %s AND team_player.id = player_id AND schedule_type_game.id = game_type_id AND schedule_schedule.id = calendar_id GROUP BY team_player.id ORDER BY points DESC", [team_id, game_type_id])
    return dictfetchall(cursor)

def player_stats_sql(player_id, division_id, game_type_id):
    cursor = connection.cursor()    
    cursor.execute("SELECT team_season.year_start, team_season.year_end, team_division.name as division_name, type_name, count(*) as games, sum(goals) as goals, sum(assists) as assists, sum(penalties) as penalties, sum(goals) + sum(assists) as points FROM stats_stat, schedule_schedule, schedule_type_game, team_team, team_division, team_season WHERE player_id = %s AND division_id = %s AND game_type_id = %s AND team_id = team_team.id AND division_id = team_division.id AND season_id = team_season.id AND calendar_id = schedule_schedule.id AND schedule_type_game.id = game_type_id GROUP BY team_season.id ORDER BY team_season.year_start DESC", [player_id, division_id, game_type_id])
    return dictfetchall(cursor)

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]