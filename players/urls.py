from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('players/', views.players, name='players'),
    path('players/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('matches/', views.matches, name='matches'),
    path('matches/matchdetails/<int:id>', views.matchdetails, name='matchdetails'),
    path('news/', views.news, name='news'),
    path('news/newsdetails/<int:id>', views.newsdetails, name='newsdetails')
]