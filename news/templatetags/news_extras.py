from django import template
from schedule.models import Schedule
import datetime

register = template.Library()

@register.inclusion_tag('news_extra.html')
def show_extra():
    last_result = Schedule.objects.filter(score_home__isnull=False).order_by('game_date').reverse()[:5]
    next_games = Schedule.objects.filter(game_date__gt=datetime.datetime.now()).order_by('game_date')[:5]
    return {'last_result': last_result, 'next_games': next_games}