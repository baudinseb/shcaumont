from django.db import models

class Division(models.Model):
    name = models.CharField(max_length=40)
    
    def __unicode__(self):
        return self.name
    
class Season(models.Model):
    year_start = models.SmallIntegerField()
    year_end = models.SmallIntegerField()
    current = models.BooleanField()
    
    def __unicode__(self):
        return u"Season {0} - {1}".format(self.year_start, self.year_end)
    
class Team(models.Model):
    name = models.CharField(max_length=80)
    short_name = models.CharField(max_length=40)
    games = models.SmallIntegerField()
    wins = models.SmallIntegerField()
    draws = models.SmallIntegerField()
    losses = models.SmallIntegerField()
    division = models.ForeignKey(Division)
    season = models.ForeignKey(Season)
    
    def __unicode__(self):
        return self.name
    
