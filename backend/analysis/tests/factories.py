import factory
from analysis.models import Country, ClimateDataActual, ClimateChangePrediction

class ClimateDataActualFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ClimateDataActual

    temperature = factory.Faker('pyfloat', min_value=-20, max_value=55)


class ClimateChangePredictionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ClimateChangePrediction

    monthly_temperature = factory.Faker('pyfloat', min_value=-20, max_value=55)


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country

    name = factory.Sequence(lambda n: 'country%d' % n)
