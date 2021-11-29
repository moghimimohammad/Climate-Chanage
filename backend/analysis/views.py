# from django.db.models.aggregates import Sum, Count, Avg
from django.shortcuts import render
from rest_framework import generics
from django.db.models import Avg, F
from rest_framework.pagination import PageNumberPagination

from analysis.models import Country
from analysis.serializer import CountrySerializer


class CountryListView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_queryset(self):
        return self.queryset.filter(
            climate_data_actuals__isnull=False,
            climate_change_predictions__isnull=False
        ).annotate(
            avg_past=Avg('climate_data_actuals__temperature'),
            avg_future=Avg('climate_change_predictions__monthly_temperature'),
            change=F('avg_future') - F('avg_past')
        ).order_by('-change')
