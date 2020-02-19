

# Thiago Lima
# Telling whether or not today is a weekday.

# Import Python's datetime module

import datetime

weekday = datetime.datetime.today().weekday() # get the day of week. 0 for monday, 6 to sunday

if weekday < 5: # if the day of the week is between monday and friday (0 to 4)
    print('Yes, unfortunately today is a weekday')

else: # if the day of the week is equal 5 or 6 (saturday or sunday)
    print('It is the weekend, yay!')
