import requests

# response = requests.get("https://lendittfinserve.com/prod/admin/emi/getUpcomingEmi?start_date=2023-09-06T10%3A00%3A00.000Z&end_date=2023-09-06T10%3A00%3A00.000Z&emiStatus=1&isCountOnly=false&download=false",verify=False)
#
# print(response.status_code)
# print(response.json())


response2 = requests.get("https://lendittfinserve.com/prod/admin/emi/repaymentStatus?fromDate=2023-09-06T10%3A00%3A00.000Z&endDate=2023-09-06T10%3A00%3A00.000Z&type=TOTAL&page=1",verify=False)
print(response2.status_code)
print(response2.json())
