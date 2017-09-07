# Hint:  use Google to find python function

#Option 1: define a new object Days, assuming 365 days in a year, 30 days in a month 
class Days(object):
    """Represents the day of the year.
    attributes: year, month, day
    """
def print_day(d):   #'%.2d' prints an integer using at least 2 digits
    print '%.2d-%.2d-%.2d' % (d.month, d.day, d.year)  
def diff_day(d1, d2):
    diff = Days()
    diff.year = d2.year - d1.year
    diff.month = d2.month - d1.month
    diff.day = d2.day - d1.day
    return diff

def days_to_day(days):
    day_year = days.year * 365 
    day_month = days.month * 30 
    day = day_year + days.day + day_month
    return day 

#option 2 - use built-in modules and functions 
from datetime import datetime

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%m-%d-%Y")
    d2 = datetime.strptime(d2, "%m-%d-%Y")
    return abs((d2 - d1).days)

days_between('01-02-2013', '07-28-2015') 
  
####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

start = Days()
start.year = 2013
start.month = 1
start.day = 2
end = Days()
end.year = 2015
end.month = 7
end.day = 28
duration = diff_day(start, end)
print_day(duration)
days_to_day(duration)

#result from option 1: 936 days 
#result from option 2: 937 days 

####b)  
#option 2: 

date_start = '12312013'  
date_stop = '05282015'

from datetime import datetime

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%m%d%Y")
    d2 = datetime.strptime(d2, "%m%d%Y")
    return abs((d2 - d1).days)

days_between(date_start, date_stop) 

#option 1: 
start = Days()
start.year = 2013
start.month = 12
start.day = 31
end = Days()
end.year = 2015
end.month = 5
end.day = 28
duration = diff_day(start, end)
print_day(duration)
days_to_day(duration)

#result from option 1: 517 days 
#result from option 2: 513 days 

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

start = Days()
start.year = 1994
start.month = 1
start.day = 15
end = Days()
end.year = 2015
end.month = 7
end.day = 14
duration = diff_day(start, end)
print_day(duration)
days_to_day(duration)

#result from option 2: 7844 days 
#result from option 1: 7810 days 
