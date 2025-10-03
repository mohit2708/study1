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
print(now)
print("year", now.year)
print("month", now.month)
print("day", now.day)
print("hour", now.hour)
print("minutes", now.minute)
print("second", now.second)

Output:- 2024-12-25 10:16:05.190706
year 2024
month 12
day 25
hour 10
minutes 53
second 3

(OR)
from datetime import datetime

# returns current date and time
now = datetime.now()
print("now = ", now)

Output:- now =  2024-12-25 10:35:43.891754
```

### Get Current Date
```python
import datetime
# get current date
current_date = datetime.date.today()
print(current_date)

(OR)
# Import date class from datetime module
from datetime import date
# Returns the current local date
today = date.today()
print("Today date is: ", today)

Output:- 2024-12-25
```

### Format change data and time
```python
from datetime import datetime

# returns current date and time
now = datetime.now().strftime("%Y/%m/%d")   # change the format
print("now = ", now)
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