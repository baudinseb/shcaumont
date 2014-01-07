from django.db import models
from team.models import Team

class Type_Game(models.Model):
    type_name = models.CharField(max_length=40)
    
    def __unicode__(self):
        return self.type_name
        
class Round(models.Model):
    round_name = models.CharField(max_length=40)
    standing = models.SmallIntegerField()
    
    def __unicode__(self):
        return self.round_name
        
class Schedule(models.Model):
    def upload_rename(instance, file_name):
        return  u"pdf_file/{0}.{1}".format(instance.id,file_name.split('.')[-1])
    
    game_date = models.DateTimeField()
    game_type = models.ForeignKey(Type_Game)
    game_round = models.ForeignKey(Round, blank=True, null=True, default=None)
    place = models.CharField(max_length=40)
    team_home = models.ForeignKey(Team, related_name="team_home")
    team_away = models.ForeignKey(Team, related_name="team_away")
    score_home = models.SmallIntegerField(blank=True, null=True)
    score_away = models.SmallIntegerField(blank=True, null=True)
    details = models.CharField(max_length=20, blank=True, null=True)
    pdf_file = models.FileField(upload_to=upload_rename, blank=True, null=True)
    
    def __unicode__(self):
        return u"{0} {1}-{2} {3}".format(self.game_date, self.team_home, self.team_away, self.game_type)
    
    
