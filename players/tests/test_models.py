from django.test import TestCase
from players.models import Player, Match, News

class testModels(TestCase):

    def setUp(self):
        self.player1 = Player.objects.create(
            firstName = "player",
            lastName = "1",
            position = "GK",
            team = "Saha Colts",
            assists = 10,
            cleanSheets = 5,
            goals= 1
        )
        self.player2 = Player.objects.create(
             firstName = "player",
            lastName = "2",
            position = "GK",
            team = "Saha Colts",
            assists = 10,
            cleanSheets = 5,
            goals= 1
        )

    def test_player_count(self):
        count = Player.playerCount()
        self.assertEqual(count, 2)