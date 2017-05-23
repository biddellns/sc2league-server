from django.test import TestCase

from uuid import uuid4

from .models import Season

# Create your tests here.
class SeasonModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_season_uuid = uuid4()
        second_season_uuid = uuid4()

        first_season = Season()
        first_season.season_number = 1
        first_season.uuid = first_season_uuid
        first_season.save()

        second_season = Season()
        second_season.season_number = 2
        second_season.uuid = second_season_uuid
        second_season.save()

        saved_seasons = Season.objects.all()
        
        self.assertEqual(saved_seasons.count(), 2)

        first_saved_season = saved_seasons[0]
        second_saved_season = saved_seasons[1]

        self.assertEqual(first_saved_season.season_number, 1)
        self.assertEqual(first_saved_season.uuid, first_season_uuid)

        self.assertEqual(second_saved_season.season_number, 2)
        self.assertEqual(second_saved_season.uuid, second_season_uuid)

