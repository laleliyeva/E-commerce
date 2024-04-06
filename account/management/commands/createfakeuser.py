from typing import Any, Optional
from django.core.management import BaseCommand
from django.contrib.auth import get_user_model
from django.core.management.base import CommandParser

from faker import Faker
User = get_user_model()

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--number', type= int , default=10)



    def handle(self, *args , **options):
        faker = Faker()
        for i in range (options['number']):
            us = User.objects.create(
                email = faker.email(),
                password = faker.password(),
                first_name = faker.first_name(),
                last_name = faker.last_name(),

            )
            print(f'{us} created')
     

