from django.test import TestCase, Client
from django.urls import reverse
from players.models import Player, News, Match

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.player = Player.objects.create(
            firstName='John',
            lastName='Doe',
            position= 'GK',
            team= 'Saha Colts', 
            assists= 10,
            cleanSheets= 1,
            goals= 5
        )
        self.match = Match.objects.create(
            opponent= "Wolves",
            hora= "A",
            date= "26/06/2025",
            lastresult= "3-0 W",
            leagueposition= "4th",
            finalscore= "2-1"
        )
        self.news = News.objects.create(
            headline= "headline test",
            article= "article test",
            likes= 10,
            shares= 10
        )
        self.players_url = reverse('players')
        self.details_url = reverse('details', args=[1])
        self.main_url = reverse('main')
        self.matches_url = reverse('matches')
        self.matchdetails_url = reverse('matchdetails', args=[1])
        self.news_url = reverse('news')
        self.newsdetails_url = reverse('newsdetails', args=[1])
    
    
    
    def test_allplayers(self):
        response = self.client.get(self.players_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'allplayers.html')

    def test_player_details(self):
        response = self.client.get(self.details_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'details.html')

    def test_main_page(self):
        response = self.client.get(self.main_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')

    def test_matches(self):
        response = self.client.get(self.matches_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'matches.html')

    def test_matchdetails(self):
        response = self.client.get(self.matchdetails_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'matchdetails.html')
    
    def test_news(self):
        response = self.client.get(self.news_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news.html')

    def test_newsdetails(self):
        response = self.client.get(self.newsdetails_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsdetails.html')

    