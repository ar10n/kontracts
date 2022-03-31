from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=64)
    inn = models.CharField(max_length=10)
    phone = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=64, blank=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.name
