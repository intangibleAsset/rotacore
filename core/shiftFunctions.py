#method for calculating shifts on a given datetime date

def getShiftOnDate(shiftDate, shiftPatternStartDate, shiftPattern):
    difference = (shiftDate - shiftPatternStartDate).days
    return shiftPattern[difference%len(shiftPattern)]
