from django.db import models

from .contract import Contract


class Shipment(models.Model):
    number = models.CharField(max_length=32)
    price = models.DecimalField(decimal_places=2, max_digits=16)
    start_date = models.DateField()
    delivery_date = models.DateField()
    pay_date = models.DateField()
    is_delivered = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    contract = models.ForeignKey(
        Contract, on_delete=models.CASCADE, related_name="shipments"
    )

    def __str__(self):
        return self.number
