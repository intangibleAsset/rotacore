from django.db import models

# Create your models here.

class Employee(models.Model):
    firstName = models.TextField(blank=True, null=True)
    lastName = models.TextField(blank=True, null=True)
    shiftLink = models.ForeignKey(Shift,on_delete=models.CASCADE)


class Shift(models.Model):
    collarNumber = models
    date = models.DateField('shift date')
    startTime = models.DateTimeField('shift start')
    endTime = models.DateTimeField('shift end')
    notes = models.TextField(blank=True, null=True)
