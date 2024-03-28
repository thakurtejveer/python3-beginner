from datetime import datetime
from datetime import timedelta
from datetime import date

# Current date and time 

curr_datetime  = datetime.now()

print(f'Current Date and time are : {curr_datetime}')

print(f'Current date is : {curr_datetime.date()}')
print(f"Current time is : {curr_datetime.time()}")

# Formatting of date time 

print(f'Formatted date time is : {curr_datetime.strftime("%Y/%m/%d %H:%M:%S")}')

# Get the day of week

weekday = curr_datetime.strftime('%A')
print(weekday)

# Add and subtract time/days 

delta = timedelta(days = 1)

one_day_in_future = curr_datetime+delta
one_day_in_past = curr_datetime - delta
print(f'One day in future : {one_day_in_future}')
print(f'One day in past : {one_day_in_past}')

weekdelta = timedelta(days = 7)

one_week_in_future = curr_datetime + weekdelta
one_week_in_past = curr_datetime - weekdelta
print(one_week_in_future)
print(one_week_in_past)


# Specific date 

specific_date = date(2024, 4, 23)

print(f'Specific date : {specific_date}')


