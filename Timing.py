import datetime

# Get the current time as a datetime object
now = datetime.datetime.now()

# Get the current hour from the datetime object
current_hour = now.hour

# Check if the current hour is greater than or equal to 10
if current_hour <= 10:
    print("Good morning!")
else:
    print("Good afternoon!")


import time
time.time()