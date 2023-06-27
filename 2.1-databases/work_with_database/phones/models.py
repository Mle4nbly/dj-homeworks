from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    image = models.CharField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()