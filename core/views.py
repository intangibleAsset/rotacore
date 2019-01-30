from django.shortcuts import render
from datetime import date #used in shift view
from datetime import datetime #used in shift view
from django.http import HttpResponseNotFound
from .models import Shift
from .forms import ShiftForm
# Create your views here.

#method for calculating shifts on a given datetime date
def getShiftOnDate(shiftDate, shiftPatternStartDate, shiftPattern):
    difference = (shiftDate - shiftPatternStartDate).days
    return shiftPattern[difference%len(shiftPattern)]

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
        startDate = datetime(2019,1,9)
    elif section == "2":
        startDate = datetime(2019,1,11)
    elif section == "3":
        startDate = datetime(2019,1,13)
    elif section == "4":
        startDate = datetime(2019,1,15)
    elif section == "5":
        startDate = datetime(2019,1,17)
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
    shift = getShiftOnDate(datetimeObjectFromInputtedDate,startDate,shiftPattern)
    weekday = datetimeObjectFromInputtedDate.strftime('%A')
    displayDate = datetimeObjectFromInputtedDate.strftime('%d/%m/%Y')


    #return context and render page
    context = {'shift':shift,'section':section,'weekday':weekday,
    'date':displayDate}
    return render(request, 'core/shift.html',context)
#shift view end----------------------------------------------------------------

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
