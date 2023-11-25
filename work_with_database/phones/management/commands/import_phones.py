import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            
            for phone in phones:
                Phone.objects.create(
                    name=phone['name'],
                    price=float(phone['price']),
                    image=phone['image'],
                    release_date=phone['release_date'],
                    lte_exists=bool(phone['lte_exists']),
                    
                )