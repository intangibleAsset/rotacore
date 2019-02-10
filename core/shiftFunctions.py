#method for calculating shifts on a given datetime date
#takes date object as first and second arguments and shiftPattern
#which is an array of strings representing various named shifts ie
#['first early, second early'] etc...
def getShiftOnDate(shiftDate, shiftPatternStartDate, shiftPattern):
    difference = (shiftDate - shiftPatternStartDate).days
    return shiftPattern[difference%len(shiftPattern)]
