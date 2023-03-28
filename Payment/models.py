from django.db import models

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10)
