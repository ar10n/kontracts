from django.db import models

from .manufacturer import Manufacturer


class Product(models.Model):
    name = models.CharField(max_length=64)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self):
        return self.name
