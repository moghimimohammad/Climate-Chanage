from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(
        'Name',
        max_length=200
    )

class ClimateDataActual(models.Model):

    temperature = models.FloatField(
        'Tempreture'
    )
    year = models.CharField(
        'Year',
        max_length=50
    )
    statistics = models.CharField(
        'statistics',
        max_length=150
    )
    country = models.ForeignKey(
        'Country',
        on_delete=models.CASCADE,
        related_name='climate_data_actuals'
    )
    iso3 = models.CharField(
        'ISO3',
        max_length=150
    )


class ClimateChangePrediction(models.Model):

    monthly_temperature = models.FloatField(
        'Montly tempreture'
    )
    year = models.CharField(
        'Year',
        max_length=50
    )
    model = models.CharField(
        'model',
        max_length=50
    )
    statistics = models.CharField(
        'statistics',
        max_length=150
    )
    country = models.ForeignKey(
        'Country',
        on_delete=models.CASCADE,
        related_name='climate_change_predictions'
    )
    iso3 = models.CharField(
        'ISO3',
        max_length=150
    )