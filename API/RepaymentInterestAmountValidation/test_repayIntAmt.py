import requests
import json


class TestRepaymentInterest:

    def test_getRepaymentIntAmt(self):
        # global
        responseAllLoanID = requests.get(
            "https://lendittfinserve.com/prod/admin/transaction/allRepaidLoans?start_date=2023-10-19T10:00:00.000Z&end_date=2023-10-19T10:00:00.000Z&page=1&pagesize=10&getTotal=true&download=true",
            verify=False)  # current date

        '''getting loan ids from Repayment '''

        loanIDs = responseAllLoanID.json()["data"]["rows"]

        # print(loanIDs)

        lIDs = []

        interest = []

        for lid in loanIDs:

            if "Loan id":
                if lid["Loan id"]:
                    lIDs.append(lid["Loan id"])
                    # print(i["Loan id"])

                else:
                    pass

            if lid["Interest"]:
                interest.append(lid["Interest"])

        print("unique lids::", lIDs)
        print('count of unique lids::', len(lIDs))

        print("interest::", interest)
        print("interestLen::", len(interest))

        # Upcoming EMI
        iLId = iter(lIDs)
        # iNLId = next(iLId)

        matchInt = []
        missInt = []
        for ei in iLId:
            response = requests.get(
                "https://lendittfinserve.com/prod/admin/loan/getEMIRepaymentDetails", params={"loanId": ei},
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
            penaltyDaysE = []
            penaltyAmountE = []
            PaidEMIAmountE = []
            totalPaidAmountE = []
            paidPenaltyAmountE = []
            totalUnpaidAmountE = []
            UnpaidEMIAmountE = []
            UnpaidPenaltyAmountE = []

            for eD in emiData:
                if "EMI date" in eD:
                    emiDateE.append(eD['EMI date'])
                    # print(i['EMI date'])

                if "EMI amount" in eD:
                    emiAmountE.append(eD['EMI amount'])

                if "Principal Amount" in eD:
                    principalAmountE.append(eD['Principal Amount'])

                if "Interest Amount" in eD:
                    interestAmountE.append(eD['Interest Amount'])

                if "Penalty days" in eD:
                    penaltyDaysE.append(eD['Penalty days'])

                if "Penalty amount" in eD:
                    penaltyAmountE.append(eD['Penalty amount'])

                if "Paid EMI amount" in eD:
                    PaidEMIAmountE.append(eD['Paid EMI amount'])

                if "Total paid amount" in eD:
                    totalPaidAmountE.append(eD['Total paid amount'])

                if "Paid Penalty amount" in eD:
                    paidPenaltyAmountE.append(eD['Paid Penalty amount'])

                if "Total unpaid amount" in eD:
                    totalUnpaidAmountE.append(eD['Total unpaid amount'])

                if "Unpaid EMI amount" in eD:
                    UnpaidEMIAmountE.append(eD['Unpaid EMI amount'])

                if "Unpaid penalty amount" in eD:
                    UnpaidPenaltyAmountE.append(eD['Unpaid penalty amount'])

                else:
                    print("error")

            print("interestAmountE::", interestAmountE)

            # iInt = iter(interest)

            # for iae in interestAmountE:
            #     if iae in iInt:
            #         matchInt.append(ei)
            #         print("interestAmountE matched with interest of transaction")
            #     else:
            #         if iae not in iInt:
            #             missInt.append(ei)
            #             print("interestAmountE not matched with interest of transaction")
            #


            for iae in interest:
                if iae in interestAmountE:
                    matchInt.append(ei)
                    print("interestAmountE matched with interest of transaction")

                if iae not in interest:
                    missInt.append(ei)
                    print("interestAmountE not matched with interest of transaction")



        print("matchInt::", matchInt)
        print("missInt::", missInt)
        #
