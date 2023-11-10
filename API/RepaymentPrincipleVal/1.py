import requests
import json


class TestRepaymentPrinciple:

    def test_getRepaymentPrinciple(self):

        responseAllLoanID = requests.get(
            "https://lendittfinserve.com/prod/admin/transaction/allRepaidLoans?start_date=2023-10-20T10:00:00.000Z&end_date=2023-10-20T10:00:00.000Z&page=1&pagesize=10&getTotal=true&download=true",
            verify=False)  # current date

        '''getting loan ids from Repayment '''

        loanIDs = responseAllLoanID.json()["data"]["rows"]
        # print(loanIDs)


        lIDs = []
        approvedAmount = []
        principleAmount = []
        matchedPrinciple = []
        missedPrinciple = []


        for lid in loanIDs:

            if lid["Loan id"]:
                lIDs.append(lid["Loan id"])
                # print(i["Loan id"])

            if lid["Approved amount"]:
                approvedAmount.append(int(float(lid["Approved amount"])))

            if lid["Principal"]:
                principleAmount.append(lid["Principal"])



        print("lids::", lIDs)
        print('count of lids::', len(lIDs))

        min_lids = min(lIDs)
        max_lids = max(lIDs)
        print("min_lids::", min_lids)
        print("max_lids::", max_lids)




        # print("approvedAmount::", approvedAmount)
        # apprAmtInt = [int(float(ap)) for ap in approvedAmount]
        # print("apprAmtInt::", apprAmtInt)
        # print("apprAmtIntLen::", len(apprAmtInt))

        print("principleAmount::", principleAmount)
        # print("principleAmountLen::", len(principleAmount))



        # matchedPrinciple = []
        # missedPrinciple = []
        #
        # for pa in lIDs:
        #     if pa in apprAmtInt:
        #         matchedPrinciple.append(lIDs)
        #
        #     # if pa not in apprAmtInt:
        #     #     missedPrinciple.append(lIDs)
        #
        # print("matchedPrinciple::",matchedPrinciple)
        # print("missedPrinciple::",missedPrinciple)



        # Upcoming EMI
        data = {
            "loanIds": [
                f"{min_lids}",
                f"{max_lids}"
            ]
        }

        response = requests.post(
            "https://lendittfinserve.com/prod/admin/loan/massEMIRepaymentDetails",
            headers={"Postman-Token": "<calculated when request is sent>",
                     "Content-Length": "<calculated when request is sent>", "Host": "<calculated when request is sent>",
                     "User-Agent": "PostmanRuntime/7.33.0", "Accept": "*/*", "Accept-Encoding": "gzip, deflate, br",
                     "Connection": "keep-alive", "Content-Type": "application/json"}, json=data,
            verify=False)  # current date

        print('status code of get Repayment::', response.status_code)
        print(response.json())
    #     sData = response.json()
    #     # jdata = json.dumps(sData,indent=2)
    #     # print(jdata)
    #
    #     # print(response.headers)
    #     # print(response.content)
    #
    #     '''getting EMIData data of Repayment '''
    #     emiData = response.json()["data"]["EMIData"]
    #     # print(emiData)
    #
    #     # EMI Data
    #     emiDateE = []
    #     emiAmountE = []
    #     principalAmountE = []
    #     interestAmountE = []
    #     penaltyDaysE = []
    #     penaltyAmountE = []
    #     PaidEMIAmountE = []
    #     totalPaidAmountE = []
    #     paidPenaltyAmountE = []
    #     totalUnpaidAmountE = []
    #     UnpaidEMIAmountE = []
    #     UnpaidPenaltyAmountE = []
    #
    #     for eD in emiData:
    #         if "EMI date" in eD:
    #             emiDateE.append(eD['EMI date'])
    #             # print(i['EMI date'])
    #
    #         if "EMI amount" in eD:
    #             emiAmountE.append(eD['EMI amount'])
    #
    #         if "Principal Amount" in eD:
    #             principalAmountE.append(eD['Principal Amount'])
    #
    #         if "Interest Amount" in eD:
    #             interestAmountE.append(eD['Interest Amount'])
    #
    #         if "Penalty days" in eD:
    #             penaltyDaysE.append(eD['Penalty days'])
    #
    #         if "Penalty amount" in eD:
    #             penaltyAmountE.append(eD['Penalty amount'])
    #
    #         if "Paid EMI amount" in eD:
    #             PaidEMIAmountE.append(eD['Paid EMI amount'])
    #
    #         if "Total paid amount" in eD:
    #             totalPaidAmountE.append(eD['Total paid amount'])
    #
    #         if "Paid Penalty amount" in eD:
    #             paidPenaltyAmountE.append(eD['Paid Penalty amount'])
    #
    #         if "Total unpaid amount" in eD:
    #             totalUnpaidAmountE.append(eD['Total unpaid amount'])
    #
    #         if "Unpaid EMI amount" in eD:
    #             UnpaidEMIAmountE.append(eD['Unpaid EMI amount'])
    #
    #         if "Unpaid penalty amount" in eD:
    #             UnpaidPenaltyAmountE.append(eD['Unpaid penalty amount'])
    #
    #         else:
    #             print("error")
    #
    #     sumOfPrincipalAmountE = sum(principalAmountE)
    #     if sumOfPrincipalAmountE:
    #         sumOfPrincipalAmountEList.append(sumOfPrincipalAmountE)
    #
    #     print("sumOfPrincipalAmountEList::", sumOfPrincipalAmountEList)
    #     print("sumOfPrincipalAmountEListLen::", len(sumOfPrincipalAmountEList))
    #
    # # if apprAmtInt == sumOfPrincipalAmountEList:
    # #     print("apprAmtInt matched with sumOfPrincipalAmountEList")
    # # else:
    # #     print("apprAmtInt not matched with sumOfPrincipalAmountEList")
    # #
    # # for nm in lIDs:
    # #     if sumOfPrincipalAmountEList:
    # #         notMatchedPA.append(nm)
    # # print("notMatchedPA::", notMatchedPA)
