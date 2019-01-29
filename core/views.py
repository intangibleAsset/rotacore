from django.shortcuts import render
from datetime import date #used in shift view
from datetime import datetime #used in shift view
# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def shift(request):


    #method for calculating shifts on a given datetime date
    def getShiftOnDate(shiftDate, shiftPatternStartDate, shiftPattern):
        difference = (shiftDate - shiftPatternStartDate).days
        return shiftPattern[difference%len(shiftPattern)]

    #get selected date and section from webpage
    section = request.GET.get("section","error")#returns section or 'error'
    inputtedDate = request.GET.get("dateSelected","error")

    #the dates shift patterns start for each section
    section2ShiftCycleStartDate = datetime(2019,1,21)

    #convert user inputted date to datetime object for comparison
    datetimeObjectFromInputtedDate = datetime.strptime(inputtedDate, '%Y-%m-%d')

    #array representing section shift pattern
    shiftPattern = ['1st Early','2nd Early','1st Late','2nd Late',
    '1st Night','2nd Night','1st Rest Day','2nd Rest Day',
    '3rd Rest Day','4th Rest Day']

    #use getShiftOnDate funcion to calculate which shift
    #individual will be on a given date
    shift = getShiftOnDate(datetimeObjectFromInputtedDate,datetime(2019,1,21),shiftPattern)
    weekday = datetimeObjectFromInputtedDate.strftime('%A')
    displayDate = datetimeObjectFromInputtedDate.strftime('%d/%m/%Y')


    #return context and render page
    context = {'shift':shift,'section':section,'weekday':weekday,
    'date':displayDate}
    return render(request, 'core/shift.html',context)
