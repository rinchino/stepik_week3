from vacancies import data
from vacancies.models import Company
from vacancies.models import Specialty
from vacancies.models import Vacancy
import os

import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'stepik_week3.settings'
django.setup()

for specialty_data in data.specialties:
    specialty = Specialty.objects.update(picture='https://place-hold.it/100x60')

for company_data in data.companies:
    Company.objects.update(logo='https://place-hold.it/100x60')

for vacancy_data in data.jobs:
    Vacancy.objects.all()
