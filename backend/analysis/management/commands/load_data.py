import csv
from copy import deepcopy
from django.core.management import BaseCommand, call_command
from analysis.models import Country, ClimateChangePrediction, ClimateDataActual 



class Command(BaseCommand):
    help = "DEV COMMAND: Load data form csv files"


    def handle(self, *args, **options):
        import csv
        rows = []
        climate_data_actuals = []
        with open("data/ClimateDataActual.csv", 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                country, _ = Country.objects.get_or_create(
                    name=row[3]
                )
                climate_data_actuals.append(
                    ClimateDataActual(
                        temperature=row[0],
                        year=row[1],
                        statistics=row[2],
                        country=country,
                        iso3=row[4]
                        
                    )

                )

                rows.append(row)
            ClimateDataActual.objects.bulk_create(
                climate_data_actuals
            )
        climate_change_prediction = []
        with open("data/ClimateChangePrediction.csv", 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                country, _ = Country.objects.get_or_create(
                    name=row[4]
                )
                climate_change_prediction.append(
                    ClimateChangePrediction(
                        monthly_temperature=row[0],
                        year=row[1],
                        model=row[2],
                        statistics=row[3],
                        country=country,
                        iso3=row[5]
                    )

                )

                rows.append(row)
            ClimateChangePrediction.objects.bulk_create(
                climate_change_prediction
            )
