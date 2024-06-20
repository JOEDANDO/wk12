from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from.models import Player

# Create your views here.
def players(request):
  myplayers = Player.objects.all().values()
  template = loader.get_template('allplayers.html')
  context = {
    'myplayers': myplayers,
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
