from django.urls import path, include


import analysis.views


urlpatterns = [
    path('countries/', analysis.views.CountryListView.as_view(), name='countries'),
]
