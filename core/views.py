from django.shortcuts import render
from datetime import date #used in shift view
from datetime import datetime #used in shift view
from datetime import timedelta#used in add employee to rota view
from django.http import HttpResponseNotFound

from .models import Shift, Employee
from .forms import ShiftForm, EmployeeForm

from . shiftFunctions import getShiftOnDate

#index view -------------------------------------------------------------------
def index(request):
    return render(request, 'core/index.html')
#index view end----------------------------------------------------------------

#display_shift view------------------------------------------------------------
def display_shift(request):
    return render(request, 'core/display_shift.html')
#display shift end-------------------------------------------------------------

#shift view -------------------------------------------------------------------
def shift(request):
    #get selected date and section from webpage
    section = request.GET.get("section","error")#returns section or 'error'
    inputtedDate = request.GET.get("dateSelected","error")

    #the dates shift patterns start for each section
    if section == "1":
        startDate = date(2019,1,9)
    elif section == "2":
        startDate = date(2019,1,11)
    elif section == "3":
        startDate = date(2019,1,13)
    elif section == "4":
        startDate = date(2019,1,15)
    elif section == "5":
        startDate = date(2019,1,17)
    else:
        return HttpResponseNotFound('<h1>Invalid section data</h1>')
    #convert user inputted date to datetime object for comparison
    datetimeObjectFromInputtedDate = datetime.strptime(inputtedDate, '%Y-%m-%d')

    #array representing section shift pattern
    shiftPattern = ['1st Early','2nd Early','1st Late','2nd Late',
    '1st Night','2nd Night','1st Rest Day','2nd Rest Day',
    '3rd Rest Day','4th Rest Day']

    #use getShiftOnDate funcion to calculate which shift
    #individual will be on a given date
    shift = getShiftOnDate(datetimeObjectFromInputtedDate.date(),startDate,shiftPattern)
    weekday = datetimeObjectFromInputtedDate.strftime('%A')
    displayDate = datetimeObjectFromInputtedDate.strftime('%d/%m/%Y')


    #return context and render page
    context = {'shift':shift,'section':section,'weekday':weekday,
    'date':displayDate}
    return render(request, 'core/shift.html',context)
#shift view end----------------------------------------------------------------
def add_employee_rota(request):
    shiftPattern = ['1st Early','2nd Early','1st Late','2nd Late',
    '1st Night','2nd Night','1st Rest Day','2nd Rest Day',
    '3rd Rest Day','4th Rest Day']
    shiftDate=datetime.now()
    for i in range(0,365):
        s = Shift(emp=Employee,date=shiftDate,startTime=shiftDate,endTime=shiftDate,notes=getShiftOnDate(shiftDate,datetime(2019,1,11),shiftPattern))
        shiftDate = shiftDate + timedelta(days=1)
        s.save()
    return render(request, 'core/add_employee_rota.html',context={})

#shift_amend_view-------------------------------------------------------------
def shift_amend_view(request):
    form = ShiftForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ShiftForm()


    print(request.POST)
    context = {
        "form":form
    }
    return render(request,"core/shift_amend.html",context)
#shift_amend_view end----------------------------------------------------------
def add_employee_view(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ShiftForm()


    print(request.POST)
    context = {
        "form":form
    }
    return render(request,"core/add_employee.html",context)
