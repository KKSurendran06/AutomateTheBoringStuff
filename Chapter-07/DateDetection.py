import re

def leapCheck(YEAR):
    return (YEAR % 4 == 0 and YEAR % 100 != 0) or (YEAR % 400 == 0)

def isValid(DAY, MONTH, YEAR):
    DAY = int(DAY)
    YEAR = int(YEAR)
    
    if MONTH in ["01", "03", "05", "07", "08", "10", "12"]:
        if DAY > 31:
            return False
    elif MONTH in ["04", "06", "09", "11"]:
        if DAY > 30:
            return False
    elif MONTH == '02':
        if leapCheck(YEAR):
            if DAY > 29:
                return False
        elif DAY > 28:
            return False
    else:
        return False
    
    return True

dateRegex = re.compile(r'(\d\d)\/(\d\d)\/(\d\d\d\d)')
mo = dateRegex.search('31/02/2020')
day = mo.group(1)
month = mo.group(2)
year = mo.group(3)

if isValid(day, month, year):
    print("Valid date")
else:
    print("Invalid date")


