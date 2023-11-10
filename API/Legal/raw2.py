import datetime

import requests
import pytest

start = datetime.datetime.strptime("2023-11-04", "%Y-%m-%d")
end = datetime.datetime.strptime("2023-11-08", "%Y-%m-%d")
# date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

previous_date = start.strftime("%Y-%m-%d")
current_date = end.strftime("%Y-%m-%d")

print("current_date::", current_date)
print("previous_date::", previous_date)






