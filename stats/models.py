from django.db import models
from team.models import Team, Season, Player, Division, Position
from schedule.models import Schedule, Round, Type_Game

class Stat(models.Model):
    player = models.ForeignKey(Player)
    calendar = models.ForeignKey(Schedule)
    team = models.ForeignKey(Team)
    goals = models.SmallIntegerField(default=0)
    assists = models.SmallIntegerField(default=0)
    penalties = models.SmallIntegerField(default=0)
    minutes = models.SmallIntegerField(blank=True, null=True, default=None)
    goals_against = models.SmallIntegerField(blank=True, null=True, default=None)
    
    def __unicode__(self):
        return u"{0} - {1}:{2}".format(self.id, self.player, self.team)

