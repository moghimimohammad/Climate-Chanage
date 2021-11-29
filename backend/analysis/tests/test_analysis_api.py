from django.test import TestCase
from rest_framework.reverse import reverse
from analysis.models import Country

from analysis.tests import factories


class AnaylysisAPITest(TestCase):
    def setUp(self) -> None:
        self.countries = factories.CountryFactory.create_batch(50)
        for country in self.countries:
            factories.ClimateDataActualFactory.create_batch(
                10,
                country=country
            )
            factories.ClimateChangePredictionFactory.create_batch(
                10,
                country=country
            )
            country.refresh_from_db()
    
    def test_list(self):
        url = reverse('countries')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        counties_qs = Country.objects.all()
        counties_result = response.data['results']
        total_result = response.data['count']

        self.assertEqual(len(counties_qs), total_result)
        self.assertEqual(10, len(counties_result))