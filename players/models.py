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

    @classmethod
    def playerCount(cls):
        return cls.objects.count()

class Match(models.Model):
    opponent = models.CharField(max_length=100)
    hora = models.CharField(max_length=1)
    date = models.CharField(max_length=20)
    lastresult = models.CharField(null=True, max_length=100)
    leagueposition = models.CharField(max_length=5)
    finalscore = models.CharField(null=True, max_length=100)

class News(models.Model):
    headline = models.CharField(max_length=800)
    article = models.CharField(max_length=2000)
    likes = models.IntegerField(null=True)
    shares = models.IntegerField(null=True)

    @classmethod
    def newsCount(cls):
        return cls.objects.count()
    