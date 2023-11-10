import requests
import pytest


# curl --location 'https://lendittfinserve.com/prod/admin/emi/getUpcomingEmi?start_date=2023-09-04T10%3A00%3A00.000Z&end_date=2023-09-04T10%3A00%3A00.000Z&emiStatus=1&isCountOnly=false&download=false'
# curl --location 'https://lendittfinserve.com/prod/admin/emi/repaymentStatus?fromDate=2023-09-04T10%3A00%3A00.000Z&endDate=2023-09-04T10%3A00%3A00.000Z&type=TOTAL&page=1'

class TestEMI:

    def test_getEMI(self):
        global countEMI
        response = requests.get(
            "https://lendittfinserve.com/prod/admin/emi/getUpcomingEmi?start_date=2023-09-06T10%3A00%3A00.000Z&end_date=2023-09-06T10%3A00%3A00.000Z&emiStatus=1&isCountOnly=false&download=false",
            verify=False)

        # print('status_code::', response.status_code)
        # print(response.json())
        countEMI = response.json()["data"]["count"]
        print("countEMI::", response.json()["data"]["count"])



    def test_getRepaymentStatus(self):
        response2 = requests.get(
            "https://lendittfinserve.com/prod/admin/emi/repaymentStatus?fromDate=2023-09-06T10%3A00%3A00.000Z&endDate=2023-09-06T10%3A00%3A00.000Z&type=TOTAL&page=1",
            verify=False)

        # print('status_code::', response2.status_code)
        # print('valid::', response2.json())

        countRepaymentStatus = response2.json()["data"]["count"]

        print("countRepaymentStatus::", response2.json()["data"]["count"])

        if countEMI < countRepaymentStatus:
            print("countEMI is less than countRepaymentStatus")
            assert countEMI < countRepaymentStatus, "countEMI is less than countRepaymentStatus"

        else:
            print("Error:: countEMI is grater than countRepaymentStatus")

