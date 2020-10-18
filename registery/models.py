from django.db import models

class DemographicInfo(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    national_code = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    cell_number = models.CharField(max_length=200)
    education_degree = models.CharField(max_length=200)
    def __str__(self):
        return self.first_name
