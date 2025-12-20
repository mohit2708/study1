### Attributes of datetime Module
```python
import datetime

print(dir(datetime))

Output:-
['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']
```

### Get Current Date and Time
```python
import datetime
# get the current date and time
now = datetime.datetime.now()
print(now)                  # Output:- 2024-12-25 10:16:05.190706
print("year", now.year)     # Output:- year 2024
print("month", now.month)   # Output:- month 12
print("day", now.day)       # Output:- day 25
print("hour", now.hour)     # Output:- hour 10
print("minutes", now.minute)# Output:- minutes 53
print("second", now.second) # Output:- second 3

(OR)
from datetime import datetime

# returns current date and time
now = datetime.now()
print("now = ", now)    # Output:- now =  2024-12-25 10:35:43.891754
```

### Get Current Date
```python
import datetime
# get current date
current_date = datetime.date.today()
print(current_date) # Output:- 2024-12-25

(OR)
# Import date class from datetime module
from datetime import date
# Returns the current local date
today = date.today()
print("Today date is: ", today) # Output:- 2024-12-25
```

### Format change data and time
```python
from datetime import datetime

# returns current date and time
now = datetime.now().strftime("%Y/%m/%d")   # change the format
print("now = ", now)    # Output:- now =  2025/12/20
```

### Do I Get a Specific Date in Python?
```python
from datetime import date

# Create a specific date
specific_date = date(2024, 12, 25)
print(specific_date)  # Output: 2024-12-25

# with time parameters as well
a = datetime(2022, 10, 22, 6, 2, 32, 5456)
print(a)  # Output:- 2022-10-22 06:02:32.005456
```

### Get the time for spacific time zone
```python
from datetime import datetime
import zoneinfo
# get the current date and time
dtobj = datetime.now()
print(dtobj)

# Convert to Eastern Time
eastern_tz = zoneinfo.ZoneInfo("America/New_York")
eastern_time = dtobj.astimezone(eastern_tz)
print(f"Eastern Time: {eastern_time}")      # Output:- Eastern Time: 2025-10-24 06:12:12.045113-04:00

# Convert to Asia Time
asia_tz = zoneinfo.ZoneInfo("Asia/Kolkata")
asia_time = dtobj.astimezone(asia_tz)
print(asia_time.strftime("%Y/%m/%d"))   # Output:- 2025/10/24
print(asia_time.strftime("%Y-%m-%d %I:%M:%S %p %Z"))    # Output:- 2025-10-24 03:49:30 PM IST
print(f"Asia Time: {asia_time}")        # Output:- Asia Time: 2025-10-24 15:42:12.045113+05:30
```

### Add hour, days, week, etc
```python
from datetime import datetime, timedelta

# Get the current date and time
dtobj = datetime.now()
print(f"Current date and time: {dtobj}")    # Output:- Current date and time: 2025-10-24 10:31:19.274839

# Add 6 days to the datetime object
future_date = dtobj + timedelta(days=6)
print(f"Date after adding 6 days: {future_date}")   # Output:- Date after adding 6 days: 2025-10-30 10:31:19.274839

# Format both dates for better readability
print(f"Today: {dtobj.strftime('%A, %B %d, %Y at %I:%M %p')}")  # Output:- Today: Friday, October 24, 2025 at 10:31 AM
print(f"After 6 days: {future_date.strftime('%A, %B %d, %Y at %I:%M %p')}") # Output:- After 6 days: Thursday, October 30, 2025 at 10:31 AM


# Add different time units
print(f"Add 1 week: {dtobj + timedelta(weeks=1)}")
print(f"Add 2 hours: {dtobj + timedelta(hours=2)}")
print(f"Add 30 minutes: {dtobj + timedelta(minutes=30)}")
print(f"Add 6 days and 3 hours: {dtobj + timedelta(days=6, hours=3)}")


# Subtract time (go back in time)
past_date = dtobj - timedelta(days=6)
print(f"6 days ago: {past_date.strftime('%A, %B %d, %Y at %I:%M %p')}")

# Calculate difference between dates
difference = future_date - dtobj
print(f"Difference: {difference}")
print(f"Difference in days: {difference.days}")
print(f"Total seconds: {difference.total_seconds()}")

# Multiple operations
complex_date = dtobj + timedelta(days=6, hours=12, minutes=30, seconds=45)
print(f"Complex addition: {complex_date}")
```

### Add month and year
```python
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Get the current date and time
dtobj = datetime.now()
print(f"Current date and time: {dtobj}")

# Add 3 months to the datetime object
future_date_3_months = dtobj + relativedelta(months=3)
print(f"Date after adding 3 months: {future_date_3_months}")

# Add 1 year and 2 months
future_date_1y_2m = dtobj + relativedelta(years=1, months=2)
print(f"Date after adding 1 year and 2 months: {future_date_1y_2m}")

# Subtract 6 months
past_date_6_months = dtobj - relativedelta(months=6)
print(f"Date after subtracting 6 months: {past_date_6_months}")

# Example with end of month handling:
# If the original day is 31 and the target month only has 30 days,
# relativedelta will correctly adjust to the last day of the target month.
print("\n--- End of month handling example ---")
date_at_month_end = datetime(2023, 1, 31)
print(f"Original date: {date_at_month_end}")
date_plus_1_month = date_at_month_end + relativedelta(months=1)
print(f"Plus 1 month (Feb): {date_plus_1_month}") # Should be Feb 28/29
date_plus_2_months = date_at_month_end + relativedelta(months=2)
print(f"Plus 2 months (Mar): {date_plus_2_months}") # Should be Mar 31

# Format for better readability
print(f"\nToday: {dtobj.strftime('%A, %B %d, %Y')}")
print(f"Plus 3 months: {future_date_3_months.strftime('%A, %B %d, %Y')}")
print(f"Minus 6 months: {past_date_6_months.strftime('%A, %B %d, %Y')}")
```

### string convert into data format
```python
from datetime import datetime

# Your string date
date_string = "2025-10-24"
print(f"Original string: {date_string}")    # Output:- Original string: 2025-10-24

# Method 1: Convert string to datetime object
date_obj = datetime.strptime(date_string, "%Y-%m-%d")
print(f"Converted to datetime: {date_obj}") # Output:- Converted to datetime: 2025-10-24 00:00:00
print(f"Type: {type(date_obj)}")    # Output:- Type: <class 'datetime.datetime'>

# Method 2: If you only need the date part (without time)
from datetime import date
date_only = datetime.strptime(date_string, "%Y-%m-%d").date()
print(f"Date only: {date_only}")    # Output:- Date only: 2025-10-24
print(f"Type: {type(date_only)}")   # Output:- Type: <class 'datetime.date'>
```

### how to difference date in python
#### Subtracting date or datetime objects:
* we can use date and datetime
```python
from datetime import date, datetime

# Example with date objects
date1 = date(2023, 1, 15)
date2 = date(2023, 2, 20)
difference_days = (date2 - date1).days
print(f"Difference in days: {difference_days}")     # Output:- Difference in days: 36

# Example with datetime objects
datetime1 = datetime(2023, 1, 15, 10, 30, 0)
datetime2 = datetime(2023, 1, 16, 12, 0, 0)
time_difference = datetime2 - datetime1
print(f"Time difference: {time_difference}")    # Output:- Time difference: 1 day, 1:30:00
print(f"Difference in seconds: {time_difference.total_seconds()}")  # Output:- Difference in seconds: 91800.0
```

* Using dateutil.relativedelta for more complex differences:
```python
from datetime import datetime
from dateutil.relativedelta import relativedelta

date_of_birth = datetime(1990, 5, 10)
current_date = datetime.now() # Or a specific date like datetime(2025, 10, 27)

age = relativedelta(current_date, date_of_birth)
print(f"Age: {age.years} years, {age.months} months, {age.days} days")      # Output:- Age: 35 years, 5 months, 17 days
```