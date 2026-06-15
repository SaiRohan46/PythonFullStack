#Hello day-26
'''
Date and Time
-------------
--> Python Provides the built in date and time module to work with date and time

import datetime
-------------


import datetime as dt
today=dt.date.today()
now=dt.datetime.now()
print(today)
print(now)

import datetime as dt
now=dt.datetime.now()
print(f"Year : {now.year}")
print(f"Month : {now.month}")
print(f"Day : {now.day}")
print(f"Hour : {now.hour}")
print(f"Minutes : {now.minute}")
print(f"Second : {now.second}")


Formatting Date and Time
-------------------------
--> strftime() is used to format date and time

%d --> day
%m --> months
%Y --> Year
%H --> Hours
%M --> Minutes
%S --> Seconds


import datetime as dt
now=dt.datetime.now()
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%H-%M-%S"))

import datetime
date1=datetime.date(2025,6,1)
date2=datetime.date(2026,6,1)
diff=date2-date1
print(diff)

TimeDelta
----------
--> Used to calculate the date after preffered number of days


import datetime
today=datetime.date.today()
future_=today + datetime.timedelta(days = 7)
print(future_)

ctime
------
import datetime as dt
day_=dt.date.today()
print(day_.ctime())

CALENDAR
------------
import calendar
import datetime
today=datetime.date.today()
year=today.year
month=today.month
print(calendar.month(year,month))
--------------
To print complete calendar

import calendar
year=2025
print(calendar.calendar(year))
--------------
import datetime
today=date.today()
print(today.isoweekday())


import calendar
import datetime
today=datetime.date.today()
year=today.year
month=today.month
print(calendar.month(year,month))

import datetime
today=datetime.date.today()
print(today.isoweekday())
'''
import smtplib
from email.message import EmailMessage
sender='rohansai4645@gmail.com'
reciever='kavs14345@gmail.com'
password='paofvpioxhtxxxpp'
msg=EmailMessage()
msg['From']=sender
msg['To']=reciever




























