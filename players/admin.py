from django.contrib import admin
from.models import Player
from.models import Match
from.models import News

# Register your models here.

class PlayerAdmin(admin.ModelAdmin):
    list_display = ("firstName", "lastName", "position", "team", "assists", "cleanSheets", "goals")

class MatchAdmin(admin.ModelAdmin):
    list_display = ("date", "opponent", "hora")

class NewsAdmin(admin.ModelAdmin):
    list_display = ("headline", "article")


admin.site.register( Player, PlayerAdmin)
admin.site.register( Match, MatchAdmin)
admin.site.register( News, NewsAdmin)
