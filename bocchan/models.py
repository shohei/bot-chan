from django.db import models
from django.forms import ModelForm

# Create your models here.

class Talk(models.Model):
    talk = models.CharField(max_length=140)

class TalkForm(ModelForm):
    class Meta:
        model = Talk


