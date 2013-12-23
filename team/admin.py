from django.contrib import admin
from team.models import Team, Division, Season

class TeamAdmin(admin.ModelAdmin):
    list_display   = ('name', 'short_name', 'season', 'division')
    list_filter    = ('name', )
    ordering       = ('season', 'division')
    search_fields  = ('name', )

class DivisionAdmin(admin.ModelAdmin):
    list_display   = ('name', )
    list_filter    = ('name', )
    ordering       = ('name', )
    search_fields  = ('name', )
    
class SeasonAdmin(admin.ModelAdmin):
    list_display   = ('year_start', 'year_end', 'current')
    list_filter    = ('current', )
    ordering       = ('year_start', )
    search_fields  = ('name', )
    
    
admin.site.register(Team, TeamAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Season, SeasonAdmin)
