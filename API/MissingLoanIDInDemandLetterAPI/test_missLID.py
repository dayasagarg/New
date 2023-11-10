import pytest
import requests

# curl --location 'https://lendittfinserve.com/prod/admin/legal/getAllLegalData?page=1&startDate=2023-09-12T10%3A00%3A00.000Z&endDate=2023-09-12T10%3A00%3A00.000Z&type=1&adminId=65'
# curl --location 'https://lendittfinserve.com/prod/admin/dashboard/todayAutoDebitData?start_date=2023-09-11T10%3A00%3A00.000Z&end_date=2023-09-11T10%3A00%3A00.000Z&status=9&page=1&Download=true'

#FAILED
#AD NOT PLACED


class TestMissedLID:
    @pytest.fixture
    def url(self):
        global response, response2
        # Auto-debit failed
        response = requests.get(
            "https://lendittfinserve.com/prod/admin/emi/repaymentStatus?fromDate=2023-11-04T10:00:00.000Z&endDate=2023-11-04T10:00:00.000Z&type=TOTAL&page=1&download=true")  # previous date

        # Demand letter (Legal)
        response2 = requests.get(
            "https://lendittfinserve.com/prod/admin/legal/getAllLegalData?page=1&startDate=2023-11-05T10%3A00%3A00.000Z&endDate=2023-11-05T10%3A00%3A00.000Z&type=1&adminId=65&download=true",
            verify=False)    #current date

    def test_getAutoDebitFailAndDemandLetter(self,url):
        #'''getting loan id of AutoDebitFail'''
        rows = []
        allEMiList = response.json()["data"]['rows']
        for el in allEMiList:
            if el["Today's EMI status"] == 'FAILED' or el["Today's EMI status"] == 'AD NOT PLACED':
                rows.append(el)

        # print('status code of get AutoDebitFail::', response.status_code)
        # print(response.json())

        autoDebitFailLoanId = []

        #''' adding loan id of AutoDebitFail api into AutoDebitFail list'''
        for i in rows:
            if "Loan ID" in i:
                autoDebitFailLoanId.append(i['Loan ID'])
                # print(i)

        print("AutoDebitFailLoanId::",autoDebitFailLoanId)
        print("Count of AutoDebitFailLoanId::", len(autoDebitFailLoanId))

        autoDebitNotPlaced = []

        for i in rows:
            if "Today's EMI status" == 'AD NOT PLACED':
                autoDebitNotPlaced.append(i)

        print("Auto Debit not placed::",autoDebitNotPlaced)
        print("Count of auto debit not placed::",len(autoDebitNotPlaced))

        # print('status code of get DemandLetter::', response2.status_code)
        # print('valid::', response2.json())

         #'''getting loan id of DemandLetter api'''
        rows2 = response2.json()["data"]["rows"]
        # print(rows2)

        demandLetterLoanId = []

        ''' adding loan id of DemandLetter api into DemandLetterLoanId list'''
        for i in rows2:
            if "Loan ID" in i:
                demandLetterLoanId.append(i['Loan ID'])

        print("DemandLetterLoanId::",demandLetterLoanId)
        print("Count of DemandLetterLoanId::", len(demandLetterLoanId))

        matchedLID = []

        for i in autoDebitFailLoanId:
            if i in demandLetterLoanId:
                matchedLID.append(i)
                # print("matchedLID ::",i)

        print("matchedLID::",matchedLID)
        print("count of matchedLID::",len(matchedLID))

        missedLID = []

        for i in autoDebitFailLoanId:
            if i not in demandLetterLoanId:
                missedLID.append(i)
                # print("missed loan id::",i)

        print("missedLID::", missedLID)
        count_of_missed_lid = len(missedLID)
        print("count of missedLID::", count_of_missed_lid)

        if count_of_missed_lid == 0:
            print("All auto-debit failed loan ids are present in demand letter")
        else:
            print("Error::Auto-debit failed loan ids are missing in demand letter")

        assert count_of_missed_lid == 0, "All auto-debit failed loan ids are present in demand letter"
