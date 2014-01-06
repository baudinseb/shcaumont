from django.contrib import admin
from team.models import Team, Division, Season, Position, Player

class PlayerInline(admin.TabularInline):
    model = Team.players.through
    extra = 8
    

class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Equipe', {'fields': ['name', 'short_name', 'season', 'division']}),
        ('Classement', {'fields': ['games', 'wins', 'draws', 'losses', 'goals_for', 'goals_against']}),
    ]
    inlines = [PlayerInline]
    list_display   = ('name', 'short_name', 'season', 'division')
    list_filter    = ('name', )
    ordering       = ('season', 'division')
    search_fields  = ('name', )

class DivisionAdmin(admin.ModelAdmin):
    list_display   = ('name', 'standing')
    list_filter    = ('name', 'standing')
    ordering       = ('standing', )
    search_fields  = ('name', )
    
class SeasonAdmin(admin.ModelAdmin):
    list_display   = ('year_start', 'year_end', 'current')
    list_filter    = ('current', )
    ordering       = ('year_start', )
    search_fields  = ('name', )
    
class PositionAdmin(admin.ModelAdmin):
    list_display   = ('name', 'standing')
    list_filter    = ('name', 'standing')
    ordering       = ('standing', )
    search_fields  = ('name', )
    
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname', 'in_activity')
    list_filter    = ('lastname', 'firstname')
    ordering       = ('-in_activity', 'lastname', 'firstname')
    search_fields  = ('lastname', 'firstname')
    
    
admin.site.register(Team, TeamAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Player, PlayerAdmin)
