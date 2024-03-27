import datetime
import calendar
import time
# print(time.time())
# print(time.asctime())
# haari=datetime.datetime.now()
# print("Year:",haari.year)
# print("Month:",haari.month)
# print("Day:",haari.day)
# print("Hour:",haari.hour)
# print("Minute:",haari.minute)


#---------------------To print entire calendar or particular month in a year --------------------
# s= calendar.prcal(2124)
# s1=calendar.month(2005,9)
# s2=calendar.isleap(2024)
# print(s)
# print(s2)
# print(s1)

#------------------------To print exact date before 89 days-----------------
x=datetime.datetime.now()
from datetime import timedelta
print(x + timedelta(days=-89))
print(x + timedelta(weeks=-2))
