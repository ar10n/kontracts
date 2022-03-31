from django.db import models

from .contract import Contract


class Claim(models.Model):
    name = models.CharField(max_length=128)
    start_date = models.DateField()
    deadline = models.DateField(blank=True, null=True)
    comment = models.TextField(blank=True)
    contract = models.ForeignKey(
        Contract, on_delete=models.CASCADE, related_name="claims"
    )

    def __str__(self):
        return self.name
