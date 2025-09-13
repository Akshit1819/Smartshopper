from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100, blank=True, null=True)
    total_weight = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField()
    currency = models.CharField(max_length=10, default="USD")
    url = models.URLField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
