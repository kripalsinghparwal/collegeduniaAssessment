from django.db import models

# Create your models here.

from django.db import models


class Players(models.Model):
    name = models.CharField(max_length=150)
    total_runs = models.IntegerField()
    out = models.IntegerField()
    balls = models.IntegerField()
    average = models.DecimalField(decimal_places=6, max_digits=10)
    strikerate = models.DecimalField(decimal_places=6, max_digits=10)

    def __str__(self):
        return str(self.name)