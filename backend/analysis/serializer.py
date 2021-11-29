from typing import Counter
from rest_framework import serializers

from analysis.models import Country


class CountrySerializer(serializers.ModelSerializer):
    avg_past = serializers.FloatField()
    avg_future = serializers.FloatField()
    change = serializers.FloatField()

    class Meta:
        model = Country
        fields = ('name', 'avg_past', 'avg_future', 'change')
        extra_kwargs = {
            'avg_past': {'decimal_places': 2},
            'avg_future': {'decimal_places': 2},
            'change': {'decimal_places': 2}
        }