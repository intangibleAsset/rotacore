from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id = models.CharField(max_length= 10, blank=True, null=True, unique=True)
    firstName = models.CharField(max_length= 10, blank=True, null=True)
    lastName = models.CharField(max_length= 10, blank=True, null=True)

    def __str__(self):
        return self.emp_id

class Shift(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField('shift date')
    startTime = models.DateTimeField('shift start')
    endTime = models.DateTimeField('shift end')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.notes
