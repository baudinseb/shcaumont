from django import forms
from django.forms import ModelForm
from stats.models import Stat

class StatsAdminForm(ModelForm):
    
    class Meta:
        model = Stat
