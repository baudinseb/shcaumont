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
    
class Position(models.Model):
    name = models.CharField(max_length=40)
    
    def __unicode__(self):
        return self.name
    
class Player(models.Model):
    def upload_rename(instance, file_name):
        return  u"pictures/{0}-{1}_{2}.{3}".format(instance.id,instance.lastname,instance.firstname,file_name.split('.')[-1])
    
    lastname = models.CharField(max_length=60)
    firstname = models.CharField(max_length=60)
    pseudo = models.CharField(max_length=60, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    number = models.SmallIntegerField(blank=True, null=True)
    position = models.ForeignKey(Position)
    picture = models.ImageField(upload_to=upload_rename, blank=True, null=True)
    pass    
    
    def __unicode__(self):
        return u"{0} {1}".format(self.firstname, self.lastname)
    
class Team(models.Model):
    name = models.CharField(max_length=80)
    short_name = models.CharField(max_length=40)
    games = models.SmallIntegerField()
    wins = models.SmallIntegerField()
    draws = models.SmallIntegerField()
    losses = models.SmallIntegerField()
    goals_for = models.SmallIntegerField()
    goals_against = models.SmallIntegerField()
    division = models.ForeignKey(Division)
    season = models.ForeignKey(Season)
    players = models.ManyToManyField(Player, blank=True, null=True, default=None)

    def __unicode__(self):
        return u"{0} ({1} - {2})".format(self.short_name, self.season.year_start, self.season.year_end)
    
    
    