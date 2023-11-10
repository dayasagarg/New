from datetime import datetime

# un_time = 1696390407
#
# loc_time = datetime.fromtimestamp(un_time) + GMT5:30
# print(loc_time)
#



now = datetime.now()

uniNow = datetime.timestamp(now)
print(uniNow)
# print(uniNow-19080)

import datetime
dt = datetime.datetime.fromtimestamp(1696390407)
print({"date": dt})


# 1696390407
# 1696403687.620558
#
# 19,080
