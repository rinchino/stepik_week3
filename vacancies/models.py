from django.db import models
from phone_field import PhoneField


class Specialty(models.Model):
    code = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    picture = models.URLField(max_length=200, blank=True, null=True)
    pass


class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=30)
    logo = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField()
    employee_count = models.IntegerField()
    pass


class Vacancy(models.Model):
    title = models.CharField(max_length=15)
    specialty = models.ForeignKey(Specialty, related_name="vacancies", on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name="vacancies", on_delete=models.CASCADE)
    skills = models.CharField(max_length=225)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()


class Application(models.Model):
    written_username = models.CharField(max_length=30)
    written_phone = PhoneField(blank=True, help_text='Contact phone number')
    written_cover_letter = models.TextField()


