from django.contrib import admin
from schedule.models import Type_Game, Round, Schedule

class TypeGameAdmin(admin.ModelAdmin):
    list_display   = ('type_name', )
    list_filter    = ('type_name', )
    ordering       = ('type_name', )
    search_fields  = ('type_name', )

class RoundAdmin(admin.ModelAdmin):
    list_display   = ('round_name', 'standing')
    list_filter    = ('round_name', )
    ordering       = ('standing', )
    search_fields  = ('round_name', )
    
class ScheduleAdmin(admin.ModelAdmin):
    list_display   = ('game_date', 'game_type', 'game_round', 'team_home', 'team_away', 'score_home', 'score_away', 'pdf_file')
    list_filter    = ('game_date', 'game_type', 'game_round', 'team_home', 'team_away')
    ordering       = ('game_date', )
    search_fields  = ('game_date', 'game_type', 'game_round', 'team_home', 'team_away')    
    
admin.site.register(Type_Game, TypeGameAdmin)
admin.site.register(Round, RoundAdmin)
admin.site.register(Schedule, ScheduleAdmin)

