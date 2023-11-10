import requests


from datetime import datetime, timedelta
sysDate = datetime.now()
# print(sysDate)
# print("Current day: ", datetime.now())
# print(datetime.now() + timedelta(days=5))


class TestMissedLIDInRepayment:
    def test_getEMIAndRepayment(self):
        # # Upcoming EMI
        # response = requests.get(
        #     "https://lendittfinserve.com/prod/admin/emi/getUpcomingEmi", params={"page":1,"pagesize":10,"start_date":f"{sysDate}","end_date":f"{sysDate}","emiStatus":2,"download":"true"},
        #     verify=False)    #current date
        #
        #
        # #'''getting loan id of Upcoming EMI'''
        # rows = response.json()["data"]["rows"]
        # # print(rows)
        #
        #
        # # print('status code of get Upcoming EMI::', response.status_code)
        # # print(response.json())
        # # print(response.json()["data"]["rows"])
        #
        # #
        # upcomingEMILoanId = []
        #
        # #''' adding loan id of Upcoming EMI api into upcomingEMILoanId list'''
        # for i in rows:
        #     if "Loan Id" in i:
        #         upcomingEMILoanId.append(i['Loan Id'])
        #         # print(i)
        #
        # print("UpcomingEMILoanId::",upcomingEMILoanId)
        # print("Count of UpcomingEMILoanId::", len(upcomingEMILoanId))


        #fromDate=2023-09-22T10:00:00.000Z&endDate=2023-09-22T10:00:00.000Z&type=TOTAL&page=1&download=true
        # # Demand letter (Legal)
        response2 = requests.get(
            "https://lendittfinserve.com/prod/admin/emi/repaymentStatus",params={"fromDate":f"{sysDate}","endDate":f"{sysDate}","type":"TOTAL","page":1,"download":"true"},
            verify=False)    #current date

        print('status code of get repayment::', response2.status_code)
        print('valid::', response2.json())

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

        # matchedLID = []
        #
        # for i in upcomingEMILoanId:
        #     if i in repaymentLoanId:
        #         matchedLID.append(i)
        #         # print("matchedLID ::",i)
        #
        # print("matchedLID::",matchedLID)
        # print("count of matchedLID::",len(matchedLID))
        #
        # missedLID = []
        #
        # for i in upcomingEMILoanId:
        #     if i not in repaymentLoanId:
        #         missedLID.append(i)
        #         # print("missed loan id::",i)
        #
        # print("missedLID::", missedLID)
        # count_of_missed_lid = len(missedLID)
        # print("count of missedLID::", count_of_missed_lid)
        #
        # if count_of_missed_lid == 0:
        #     print("All upcoming EMI Loan IDs are present in repayment API")
        # else:
        #     print("Error::Upcoming EMI Loan IDs are missing in repayment API")
        #
        # assert count_of_missed_lid == 0, "All upcoming EMI Loan IDs are present in repayment API"
        #




#
#
#
#
# from datetime import datetime, timedelta
# print("Current day: ", datetime.now())
# print(datetime.now() + timedelta(days=5, hours=-5))


