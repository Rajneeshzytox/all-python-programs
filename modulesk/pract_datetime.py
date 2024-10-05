# import tkinter
import datetime as d
# MAXYEAR, MINYEAR, UTC, date, datetime, datetime_CAPI, time, timedelta, timezone, tzinfo,

for i in dir(d.datetime):
    if(i.startswith('__')==True):
        continue
    print(i, end=", ")


'''
| -------------------------------
| DateTime: (Methods)
|  [ astimezone, combine, ctime, date, day, dst, fold, fromisocalendar, fromisoformat, fromordinal, fromtimestamp, hour, isocalendar, isoformat, isoweekday, max, microsecond, min, minute, month, now, replace, resolution, second, strftime, strptime, time, timestamp, timetuple, timetz, today, toordinal, tzinfo, tzname, utcfromtimestamp, utcnow, utcoffset, utctimetuple, weekday, year ]
| -------------------------------
|
|
'''
# print(help(d.datetime))