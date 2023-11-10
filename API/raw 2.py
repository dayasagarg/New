import requests
from datetime import datetime,timedelta
from requests.auth import HTTPBasicAuth

currentFullTime = datetime.now() # whole date
currentDateStr = datetime.strftime(currentFullTime,"%Y-%m-%d") # date to string format


currentDateF = datetime.strptime(currentDateStr,"%Y-%m-%d") # string to date format
currentDateFUnix = round(datetime.timestamp(currentDateF))

previousDate = currentDateF - timedelta(days=1)
previousDateStr = datetime.strftime(previousDate,"%Y-%m-%d")
previousDateF = datetime.strptime(previousDateStr,"%Y-%m-%d") # string to date format
previousDateFUnix = round(datetime.timestamp(previousDateF))



# print("currentDateFormat::",currentDateF)
# print("currentDateStr::",currentDateStr)
# print("currentDateFUnix::",currentDateFUnix)
# # print("previousDate::",previousDate)
# print("previousDateStr::",previousDateStr)
# print("previousDateFUnix::",previousDateFUnix)







print(razPay1.json())
print(razPay2.json())
# # print(response2.json())
# print(response5.json())
# print(response4.json())