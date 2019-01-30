from django.db import models

# Create your models here.
class Shift(models.Model):
    collarNumber = models.IntegerField()
    date = models.DateField('shift date')
    startTime = models.DateTimeField('shift start')
    endTime = models.DateTimeField('shift end')
    notes = models.TextField(blank=True, null=True)
