from django.db import models

class News(models.Model):
    author = models.CharField(max_length=80)
    pub_date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='date published')
    title = models.CharField(max_length=100)
    text = models.TextField()
    
    def __unicode__(self):
        return self.title
