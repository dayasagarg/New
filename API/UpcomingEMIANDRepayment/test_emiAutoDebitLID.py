import pytest
import requests

# ?page=1&pagesize=10&start_date=2023-09-22T10:00:00.000Z&end_date=2023-09-22T10:00:00.000Z&emiStatus=2&download=true
class TestMissedLIDInRepayment:
    @pytest.fixture
    def url(self):
        global response, response2
        # Upcoming EMI
        response = requests.get(
            "https://lendittfinserve.com/admin-prod/admin/emi/getUpcomingEmi",
            params={"page": 1, "pagesize": 10, "start_date": "2023-11-01T10:00:00.000Z",
                    "end_date": "2023-11-01T10:00:00.000Z", "emiStatus": 2, "download": "true"},
            verify=False)  # current date

        response2 = requests.get(
            "https://lendittfinserve.com/admin-prod/admin/emi/repaymentStatus?fromDate=2023-11-01T10:00:00.000Z&endDate=2023-11-01T10:00:00.000Z&type=TOTAL&page=1&download=true",
            verify=False)  # current date


    def test_getEMIAndRepayment(self,url):
        #'''getting loan id of Upcoming EMI'''
        rows = response.json()["data"]["rows"]
        # print(rows)

        # print('status code of get Upcoming EMI::', response.status_code)
        # print(response.json())
        # print(response.json()["data"]["rows"])




        upcomingEMILoanId = []

        #''' adding loan id of Upcoming EMI api into upcomingEMILoanId list'''
        for i in rows:
            if "Loan Id" in i:
                upcomingEMILoanId.append(i['Loan Id'])
                # print(i)

        print("UpcomingEMILoanId::",upcomingEMILoanId)
        print("Count of UpcomingEMILoanId::", len(upcomingEMILoanId))




        # # Demand letter (Legal)

        # print('status code of get repayment::', response2.status_code)
        # print('valid::', response2.json())

         #'''getting loan id of repayment api'''
        rows2 = response2.json()["data"]["rows"]
        # print(rows2)

        repaymentLoanId = []


        ''' adding loan id of repayment api into repaymentLoanId list'''
        for i in rows2:
            if "Loan ID" in i:
                repaymentLoanId.append(i['Loan ID'])

        print("RepaymentLoanId::",repaymentLoanId)
        print("Count of repaymentLoanId::", len(repaymentLoanId))


        duplicateRepaymentLoanId = []
        for du in repaymentLoanId:
            if du in duplicateRepaymentLoanId:
                pass
            else:
                duplicateRepaymentLoanId.append(du)

        print("duplicateRepaymentLoanId::", duplicateRepaymentLoanId)
        print("count_duplicateRepaymentLoanId::", len(duplicateRepaymentLoanId))


        matchedLID = []

        for i in upcomingEMILoanId:
            if i in repaymentLoanId:
                matchedLID.append(i)
                # print("matchedLID ::",i)

        print("matchedLID::",matchedLID)
        print("count of matchedLID::",len(matchedLID))

        missedLID = []

        for i in upcomingEMILoanId:
            if i not in repaymentLoanId:
                missedLID.append(i)
                # print("missed loan id::",i)

        print("missedLID::", missedLID)
        count_of_missed_lid = len(missedLID)
        print("count of missedLID::", count_of_missed_lid)

        if count_of_missed_lid == 0:
            print("All upcoming EMI Loan IDs are present in repayment API")
        else:
            print("Error::Upcoming EMI Loan IDs are missing in repayment API")

        assert count_of_missed_lid == 0, "All upcoming EMI Loan IDs are present in repayment API / auto-debit list"

