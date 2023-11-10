import requests
import json
import math
# sample LIDs:430144,572277,532329

lIDs = []
f_lid = []


class TestRepayStatus:
    def test_getRepayment(self):
        global totalUnpaidAmountForm
        responseAllLoanID = requests.get(
            "https://lendittfinserve.com/admin-prod/admin/transaction/allRepaidLoans?start_date=2023-11-04T10:00:00.000Z&end_date=2023-11-04T10:00:00.000Z&page=1&pagesize=10&getTotal=true&download=true",
            verify=False)  # current date

        '''getting loan ids from Repayment'''
        loanIDs = responseAllLoanID.json()["data"]["rows"]
        # print(loanIDs)
        emiUnpaidStatusUId = []
        for lid in loanIDs:
            if "Loan id":
                if lid["Loan id"] not in lIDs:

                    lIDs.append(lid["Loan id"])
                    # print(i["Loan id"])

                else:
                    pass

        # print("unique lids::", lIDs)
        # print('count of unique lids::', len(lIDs))


            # Upcoming EMI
            for i in lIDs:
                response = requests.get(
                    "https://lendittfinserve.com/admin-prod/admin/loan/getEMIRepaymentDetails", params={"loanId": i},
                    verify=False)  # current date

                # print('status code of get Repayment::', response.status_code)
                # print(response.json())
                sData = response.json()
                jdata = json.dumps(sData,indent=2)
                # print(jdata)

                # print(response.headers)
                # print(response.content)

                '''getting EMIData data of Repayment '''
                emiData = response.json()["data"]["EMIData"]
                # print(emiData)


                # EMI Data

                emiPaidStatusUId = []
                emiUnpaidStatusUId = []

                for eD in emiData:
                    if eD["Status"] == "Unpaid":
                        emiUnpaidStatusUId.append(lid['userId'])

                    # if eD["Status"] == "Unpaid":
                    #     emiUnpaidStatusUId.append(lid['userId'])

                    else:
                        print("error")

                # print("emiPaidStatusUId::", emiPaidStatusUId)
        print("emiUnpaidStatusUId::", emiUnpaidStatusUId)


                # uniqueUnpaidUId = []
                # for index,un in enumerate(emiUnpaidStatusUId):
                #     if index == 0:
                #         uniqueUnpaidUId.append(un)






                # for st in emiStatus:
                #     if st == "Paid":









                # ['Unpaid', 'Paid']











