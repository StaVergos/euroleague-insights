from django.db import models


class Club(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, blank=True)
    country_code = models.CharField(max_length=3, blank=True)
    country_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
