import requests
import json


class TestRepaymentPrinciple:

    def test_getRepaymentPrinciple(self):
        global totalUnpaidAmountForm, sumOfPrincipalAmountEList, principalAmountE, lid, i, eD, notMatchedPA, aa, bb
        responseAllLoanID = requests.get(
            "https://lendittfinserve.com/prod/admin/transaction/allRepaidLoans?start_date=2023-10-21T10:00:00.000Z&end_date=2023-10-21T10:00:00.000Z&page=1&pagesize=10&getTotal=true&download=true",
            verify=False)  # current date

        '''getting loan ids from Repayment '''

        loanIDs = responseAllLoanID.json()["data"]["rows"]

        # print(loanIDs)

        notMatchedPA = []
        lIDs = []
        approvedAmount = []

        principleAmountTran = []
        approvedAmount = []
        for lid in loanIDs:

            if lid["Loan id"]:
                lIDs.append(lid["Loan id"])
                # print(i["Loan id"])

            if lid["Approved amount"]:
                approvedAmount.append(lid["Approved amount"])

            if lid["Principal"]:
                principleAmountTran.append(lid["Principal"])

        print(" lids::", lIDs)
        print('count of lids::', len(lIDs))

        apprAmtInt = [int(float(ap)) for ap in approvedAmount]
        print("apprAmtInt::", apprAmtInt)
        print("apprAmtIntLen::", len(apprAmtInt))

        # Upcoming EMI
        sumOfPrincipalAmountEList = []
        for li in lIDs:
            response = requests.get(
                "https://lendittfinserve.com/prod/admin/loan/getEMIRepaymentDetails", params={"loanId": li},
                verify=False)  # current date

            # print('status code of get Repayment::', response.status_code)
            # print(response.json())
            sData = response.json()
            # jdata = json.dumps(sData,indent=2)
            # print(jdata)

            # print(response.headers)
            # print(response.content)

            '''getting EMIData data of Repayment '''
            emiData = response.json()["data"]["EMIData"]
            # print(emiData)

            # EMI Data
            emiDateE = []
            emiAmountE = []

            principalAmountE = []
            interestAmountE = []
            missed = []

            for eD in emiData:
                if "EMI date" in eD:
                    emiDateE.append(eD['EMI date'])
                    # print(i['EMI date'])

                if "EMI amount" in eD:
                    emiAmountE.append(eD['EMI amount'])

                if eD["Principal Amount"]:
                    principalAmountE.append(eD['Principal Amount'])


            # print("principalAmountE::", principalAmountE)


            sumOfPrincipalAmountE = sum(principalAmountE)
            if sumOfPrincipalAmountE:
                sumOfPrincipalAmountEList.append(sumOfPrincipalAmountE)

        print("sumOfPrincipalAmountEList::", sumOfPrincipalAmountEList)
        print("sumOfPrincipalAmountEListLen::", len(sumOfPrincipalAmountEList))

        if apprAmtInt == sumOfPrincipalAmountEList:
            print("apprAmtInt matched with sumOfPrincipalAmountEList")
        else:
            print("apprAmtInt not matched with sumOfPrincipalAmountEList")
            assert False
