import os

import django

from vacancies import data
from vacancies.models import Company
from vacancies.models import Specialty
from vacancies.models import Vacancy

os.environ["DJANGO_SETTINGS_MODULE"] = 'stepik_week3.settings'
django.setup()

for specialty_data in data.specialties:
   # specialty = Specialty.objects.create(
   #     code=specialty_data["code"],
   #     title=specialty_data['title'],
    ##)
     specialty = Specialty.objects.update(picture='https://place-hold.it/100x60')

for company_data in data.companies:
    #company = Company.objects.create(
    #    name=company_data['name'],
    #    location=company_data['location'],
    #    logo=company_data['logo'],
    #    description=company_data['description'],
    #    employee_count=company_data['employee_count'],
    #)
    Company.objects.update(logo='https://place-hold.it/100x60')

for vacancy_data in data.jobs:
    #vacancy = Vacancy.objects.create(
    #    title=vacancy_data['title'],
    #    specialty=specialty,
   #     company=company,
    #    skills=vacancy_data['skills'],
    #    description=vacancy_data['description'],
    #    salary_min=vacancy_data['salary_min'],
    #    salary_max=vacancy_data['salary_max'],
    #    published_at=vacancy_data['published_at']
    #)
     Vacancy.objects.all()
