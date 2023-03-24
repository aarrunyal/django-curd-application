from django.db import models
from django.utils import timezone

# Create your models here.
class PriceHistory(models.Model):
    date = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    volume = models.DecimalField(max_digits=7, decimal_places=3)