from django import forms

from .models import Shift, Employee

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = [
            'emp',
            'date',
            'startTime',
            'endTime',
            'notes'
        ]

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'emp_id',
            'firstName',
            'lastName'
        ]
