from django.contrib import admin
from . models import Shift
from . models import Employee
# Register your models here.
admin.site.register(Employee)
admin.site.register(Shift)
