from django.test import TestCase

from .models import League

# Create your tests here.
class LeagueModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_league = League()
        first_league.name = "Very first league"
        first_league.abbreviation = "ABC"
        first_league.save()

        second_league = League()
        second_league.name = "The second league"
        second_league.abbreviation = "DEF"
        second_league.save()

        saved_leagues = League.objects.all()

        self.assertEqual(saved_leagues.count(), 2)

        first_saved_league = saved_leagues[0]
        second_saved_league = saved_leagues[1]

        self.assertEqual(first_saved_league.name, "Very first league")
        self.assertEqual(first_saved_league.abbreviation, "ABC")

        self.assertEqual(second_saved_league.name, "The second league")
        self.assertEqual(second_saved_league.abbreviation, "DEF")
