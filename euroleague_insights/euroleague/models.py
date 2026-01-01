from django.db import models


class Club(models.Model):
    id = models.AutoField(primary_key=True)
    club_code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, blank=True)
    country_code = models.CharField(max_length=3, blank=True)
    country_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, unique=True)
    fullname = models.CharField(max_length=50)
    passport_name = models.CharField(max_length=50, blank=True)
    passport_surname = models.CharField(max_length=50, blank=True)
    jersey_name = models.CharField(max_length=50, null=True, blank=True)
    country_code = models.CharField(max_length=3)
    country_name = models.CharField(max_length=100)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    birth_date = models.DateTimeField(blank=True)
    current_club = models.ForeignKey(
        Club,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.fullname
