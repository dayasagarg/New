import pytest
import requests
from datetime import datetime,timedelta

from datetime import datetime, timedelta

currentFullTime = datetime.now() # whole date
currentDateStr = datetime.strftime(currentFullTime,"%Y-%m-%d") # date to string format
currentDateF = datetime.strptime(currentDateStr,"%Y-%m-%d") # string to date format

previousDate = currentDateF - timedelta(days=1)
previousDateStr = datetime.strftime(previousDate,"%Y-%m-%d")

previousDate_2 = currentDateF - timedelta(days=2)
previousDateStr_2 = datetime.strftime(previousDate_2,"%Y-%m-%d")

previousDate_6 = currentDateF - timedelta(days=6)
previousDateStr_6 = datetime.strftime(previousDate_6,"%Y-%m-%d")

# print("currentDateFormat::",currentDateF)
print("currentDateStr::",currentDateStr)
# print("previousDate::",previousDate)
print("previousDateStr::",previousDateStr)
print("previousDateStr_2::",previousDateStr_2)
print("previousDateStr_6::",previousDateStr_6)