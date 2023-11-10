import requests
import pytest


# curl --location 'https://lendittfinserve.com/prod/admin/emi/getUpcomingEmi?start_date=2023-09-04T10%3A00%3A00.000Z&end_date=2023-09-04T10%3A00%3A00.000Z&emiStatus=1&isCountOnly=false&download=false'
# curl --location 'https://lendittfinserve.com/prod/admin/emi/repaymentStatus?fromDate=2023-09-04T10%3A00%3A00.000Z&endDate=2023-09-04T10%3A00%3A00.000Z&type=TOTAL&page=1'

class TestEMI:

    def test_getEMIAndgetRepaymentStatus(self):

        response = requests.get(
            "https://lendittfinserve.com/prod/admin/emi/getUpcomingEmi?start_date=2023-09-08T10%3A00%3A00.000Z&end_date=2023-09-08T10%3A00%3A00.000Z&emiStatus=1&isCountOnly=false&download=false",
            verify=False)

        # print('status code of get EMI::', response.status_code)
        # print(response.json())
        # print(response.json()["data"]["rows"])
        rows = response.json()["data"]["rows"]
        lid = []

        for i in rows:
            if "Loan Id" in i:
                lid.append(i['Loan Id'])
                # print(i)

        # print(lid)
        #
        response2 = requests.get(
            "https://lendittfinserve.com/prod/admin/emi/repaymentStatus?fromDate=2023-09-08T10%3A00%3A00.000Z&endDate=2023-09-08T10%3A00%3A00.000Z&type=TOTAL&page=1",
            verify=False)

        # print('status code of get RepaymentStatus::', response2.status_code)  Loan ID
        # print('valid::', response2.json())

        rows2 = response2.json()["data"]["rows"]
        lid2 = []

        for i in rows2:
            if "Loan ID" in i:
                lid2.append(i['Loan ID'])

        # print(lid2)

        for i in lid:
            if i  in lid2:
                print(i)


# 550565
# 547185










