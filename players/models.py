from django.db import models

# Create your models here.

class Player(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    goals = models.IntegerField(null=True)
    assists = models.IntegerField(null=True)
    cleanSheets = models.IntegerField(null=True)
    