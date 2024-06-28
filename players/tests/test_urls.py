from django.test import TestCase
from django.urls import reverse, resolve
from players.views import main, players, details, matches, matchdetails, news, newsdetails

class TestUrls(TestCase):
    
    def test_main_url_is_resolved(self):
        url = reverse('main')
        self.assertEqual(resolve(url).func, main)

    def test_players_url_is_resolved(self):
        url = reverse('players')
        self.assertEqual(resolve(url).func, players)

    def test_details_url_is_resolved(self):
        url = reverse('details', args=[1])
        self.assertEqual(resolve(url).func, details)

    def test_matches_url_is_resolved(self):
        url = reverse('matches')
        self.assertEqual(resolve(url).func, matches)

    def test_matchdetails_url_is_resolved(self):
        url = reverse('matchdetails', args=[1])
        self.assertEqual(resolve(url).func, matchdetails)

    def test_news_url_is_resolved(self):
        url = reverse('news')
        self.assertEqual(resolve(url).func, news)

    def test_newsdetails_url_is_resolved(self):
        url = reverse('newsdetails', args=[1])
        self.assertEqual(resolve(url).func, newsdetails)