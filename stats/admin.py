from django.contrib import admin
from team.models import Player
from stats.models import Stat
from stats.forms import StatsAdminForm

class StatAdmin(admin.ModelAdmin):
    form = StatsAdminForm
    list_display   = ('calendar', 'team', 'player', 'goals', 'assists', 'penalties')
    list_filter    = ('calendar', 'team', 'player')
    ordering       = ('calendar', 'team', 'player')
    search_fields  = ('calendar', 'team', 'player')    
    
admin.site.register(Stat, StatAdmin)
