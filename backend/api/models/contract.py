from django.db import models

from .client import Client
from .company import Company
from .region import Region
from .product import Product


class Contract(models.Model):
    number = models.CharField(max_length=64)
    notice_number = models.CharField(max_length=32, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=24, decimal_places=2)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="contracts"
    )
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="contracts"
    )
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="contracts"
    )
    is_done = models.BooleanField(default=False)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.number
