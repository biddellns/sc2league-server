from django.test import TestCase

from seasons.models import Season

# Create your tests here.
class SeasonModelTest(TestCase):
    def test_saving_and_retrieving_items(self):        
        first_season = Season()
        first_season.season_number = 1
        first_season.uuid = 1
        first_season.save()

        second_season = Season()
        second_season.season_number = 2
        second_season.uuid = 2
        second_season.save()

        saved_seasons = Season.objects.all()
        
        self.assertEqual(saved_seasons.count(), 2)

        first_saved_season = saved_seasons[0]
        second_saved_season = saved_season[1]

        self.assertEqual(first_saved_season.season_number, 1)
        self.assertEqual(first_saved_season.uuid, 01)

        self.assertEqual(second_saved_season.season_number, 2)
        self.assertEqual(second_saved_season.uuid, 02)

