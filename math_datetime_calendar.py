# math_datetime_calendar.py
import math
import datetime
import calendar

# Math operations
print("Pi:", math.pi)
print("Square root of 25:", math.sqrt(25))

# Date and Time
current_date = datetime.datetime.now()
print("Current Date and Time:", current_date)

# Calendar
month = 5  # May
year = 2025
print(f"Calendar for {calendar.month_name[month]} {year}:\n", calendar.month(year, month))
