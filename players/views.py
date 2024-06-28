from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from.models import Player
from .models import Match
from .models import News

# Create your views here.
def players(request):
  myplayers = Player.objects.all().values()
  playerCount = Player.playerCount()
  template = loader.get_template('allplayers.html')
  context = {
    'myplayers': myplayers,
    'playerCount': playerCount
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  myplayer = Player.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myplayer': myplayer,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'footballers': ['Messi', 'Ronaldo', 'Neymar'],   
  }
  return HttpResponse(template.render(context, request))

def matches(request):
  mymatches = Match.objects.all().values()
  template = loader.get_template('matches.html')
  context = {
    'mymatches': mymatches,
  }
  return HttpResponse(template.render(context, request))

def matchdetails(request, id):
  mymatch = Match.objects.get(id=id)
  template = loader.get_template('matchdetails.html')
  context = {
    'mymatch': mymatch,
  }
  return HttpResponse(template.render(context, request))

def news(request):
  mynews = News.objects.all().values()
  newsCount = News.newsCount()
  template = loader.get_template('news.html')
  context = {
    'mynews': mynews,
    'newsCount' : newsCount
  }
  return HttpResponse(template.render(context, request))

def newsdetails(request, id):
  myarticle = News.objects.get(id=id)
  template = loader.get_template('newsdetails.html')
  context = {
    'myarticle': myarticle,
  }
  return HttpResponse(template.render(context, request))

