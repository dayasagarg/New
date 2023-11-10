import requests
import json
import math
# sample LIDs:430144,572277,532329

lIDs = []
f_lid = []


class TestRepayment:
    def test_getRepayment(self):
        global totalUnpaidAmountForm
        responseAllLoanID = requests.get(
            "https://lendittfinserve.com/admin-prod/admin/transaction/allRepaidLoans?start_date=2023-11-09T10:00:00.000Z&end_date=2023-11-09T10:00:00.000Z&page=1&pagesize=10&getTotal=true&download=true",
            verify=False)  # current date

        '''getting loan ids from Repayment'''
        loanIDs = responseAllLoanID.json()["data"]["rows"]
        # print(loanIDs)

        for lid in loanIDs:

            if "Loan id":
                if lid["Loan id"] not in lIDs:

                    lIDs.append(lid["Loan id"])
                    # print(i["Loan id"])

                else:
                    pass

        print("unique lids::", lIDs)
        print('count of unique lids::', len(lIDs))

        missMatchOfPaid = []
        missMatchOfUnpaid = []
        # Upcoming EMI
        for i in lIDs:

            response = requests.get(
                "https://lendittfinserve.com/admin-prod/admin/loan/getEMIRepaymentDetails", params={"loanId": i},
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

            ## emiDate = response.json()["data"]["EMIData"][0]["EMI date"]
            ## emiAmount = response.json()["data"]["EMIData"][0]["EMI amount"]
            ## principalAmount = response.json()["data"]["EMIData"][0]["Principal Amount"]
            ## interestAmount = response.json()["data"]["EMIData"][0]["Interest Amount"]
            ## penaltyDays = response.json()["data"]["EMIData"][0]["Penalty days"]
            ## penaltyAmount = response.json()["data"]["EMIData"][0]["Penalty amount"]
            # totalPaidAmount = response.json()["data"]["EMIData"][0]["Total paid amount"]
            # paidPenaltyAmount = response.json()["data"]["EMIData"][0]["Paid Penalty amount"]
            ## totalUnpaidAmount = response.json()["data"]["EMIData"][0]["Total unpaid amount"]
            ## UnpaidEMIAmount = response.json()["data"]["EMIData"][0]["Unpaid EMI amount"]
            ## UnpaidPenaltyAmount = response.json()["data"]["EMIData"][0]["Unpaid penalty amount"]

            # print('emiDate::',emiDate,'emiAmount::','emiAmount::','emiAmount::',emiAmount,'principalAmount::',principalAmount,'interestAmount::',interestAmount,'penaltyDays::',penaltyDays,'penaltyAmount::',penaltyAmount,'totalPaidAmount::',totalPaidAmount,'paidPenaltyAmount::',paidPenaltyAmount,'totalUnpaidAmount::',totalUnpaidAmount,'UnpaidEMIAmount::',UnpaidEMIAmount,'UnpaidPenaltyAmount::',UnpaidPenaltyAmount)
            # print('totalPaidAmount::',totalPaidAmount)

            # EMI Data
            emiDateE = []
            emiAmountE = []
            principalAmountE = []
            interestAmountE = []
            penaltyDaysE = []
            penaltyAmountE = []
            bounceChargeE = []
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

                if "Bounce charge" in eD:
                    bounceChargeE.append(eD['Bounce charge'])

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

            # print('EMI DATA:>','emiDate::',emiDateE,'emiAmount::',emiAmountE,'principalAmount::',principalAmountE,'interestAmount::',interestAmountE,'penaltyDays::',penaltyDaysE,'penaltyAmount::',penaltyAmountE,'totalPaidAmount::',totalPaidAmountE,'paidPenaltyAmount::',paidPenaltyAmountE,'totalUnpaidAmount::',totalUnpaidAmountE,'UnpaidEMIAmount::',UnpaidEMIAmountE,'UnpaidPenaltyAmount::',UnpaidPenaltyAmountE)

            # print("totalPaidAmountE::",sum(totalPaidAmountE))
            # print("emiAmountE::", sum(emiAmountE))
            # print("totalUnpaidAmountE::", sum(totalUnpaidAmountE))

            '''getting transactionData data of Repayment'''
            tranData = response.json()["data"]["transactionData"]
            # print(tranData)

            # Transaction data
            tPaidAmount = []
            tPrincipalAmount = []
            tPrincipalDifference = []
            tInterestAmount = []
            tInterestDifference = []
            tPenaltyAmount = []

            tPenaltyDifference = []

            for td in tranData:
                if td["status"] == "COMPLETED":
                    if "paidAmount" in td:
                        tPaidAmount.append(td['paidAmount'])
                        # print(i['EMI date'])

                    if "principalAmount" in td:
                        tPrincipalAmount.append(td['principalAmount'])

                    if "principalDifference" in td:
                        tPrincipalDifference.append(td['principalDifference'])

                    if "interestAmount" in td:
                        tInterestAmount.append(td['interestAmount'])

                    if "interestDifference" in td:
                        tInterestDifference.append(td['interestDifference'])

                    if "penaltyAmount" in td:
                        tPenaltyAmount.append(td['penaltyAmount'])

                    if "penaltyDifference" in td:
                        tPenaltyDifference.append(td['penaltyDifference'])

            # print('TRANSACTION DATA:>','paidAmount::',paidAmount,'principalAmount::',principalAmount,'principalDifference::',principalDifference,'interestAmount::',interestAmount,'interestDifference::',interestDifference,'penaltyAmount::',penaltyAmount,'penaltyDifference::',penaltyDifference)

            ## '''getting fullPay data of Repayment'''
            ## fullPayment = response.json()["data"]["fullPay"]
            ## print('fullPayment or net payable::',fullPayment)

            totalAmountToBePaidAdd = emiAmountE + penaltyAmountE + bounceChargeE
            totalAmountToBePaidForm = sum(totalAmountToBePaidAdd) + .0
            print("totalAmountToBePaidForm::", totalAmountToBePaidForm)

            totalPaidAmountT = math.ceil(sum(tPaidAmount))
            print("totalPaidAmountInTran::", totalAmountToBePaidForm)
            diffOfTotalPaidAmtEAndPaidAmtTran = sum(totalPaidAmountE) - totalPaidAmountT
            print("Difference between total paid amount in EMI and paid amount in transaction:: ",
                  diffOfTotalPaidAmtEAndPaidAmtTran)

            # assert sum(totalPaidAmountE)+.0 == totalPaidAmountT, "Total amount paid in EMI data is as per formula"

            totalUnpaidAmountForm = (totalAmountToBePaidForm - totalPaidAmountT)
            print("totalUnpaidAmountForm::", totalUnpaidAmountForm)
            # assert sum(totalUnpaidAmountE) == totalUnpaidAmountForm, "Total unpaid amount in EMI data is as per formula"

            print("totalUnpaidAmountE::", sum(totalUnpaidAmountE))
            diffOfTotalUnpaidAmtFormAndEMI = totalUnpaidAmountForm - (sum(totalUnpaidAmountE))
            print("Difference between totalUnpaidAmountForm and totalUnpaidAmountE:: ", diffOfTotalUnpaidAmtFormAndEMI)
            # print("UnpaidEMIAmountE::", sum(UnpaidEMIAmountE))
            # print("UnpaidPenaltyAmountE::", sum(UnpaidPenaltyAmountE))

            diffOfTotalUnpaidAmtFormAndEMIPenalty = totalUnpaidAmountForm - (
                        sum(UnpaidEMIAmountE) + sum(UnpaidPenaltyAmountE))
            print("Difference between totalUnpaidAmountForm and sum of unpaid EMI,Penalty::",
                  diffOfTotalUnpaidAmtFormAndEMIPenalty)

            if sum(totalPaidAmountE) == totalPaidAmountT:
                print(f"Total amount paid in EMI data is as per formula::Loan ID::{i}")
            else:
                missMatchOfPaid.append(i)
                print(f"Error::Total amount paid in EMI data is not as per formula::Loan ID::{i}")

            if sum(totalUnpaidAmountE) == totalUnpaidAmountForm:
                print(f"Total unpaid amount in EMI data is as per formula::Loan ID::{i}")
            else:
                missMatchOfUnpaid.append(i)
                print(f"Error::Total unpaid amount in EMI data is not as per formula::Loan ID::{i}")

            if sum(totalUnpaidAmountE) == sum(UnpaidEMIAmountE) + sum(UnpaidPenaltyAmountE):
                print(
                    f"Total unpaid amount in EMI data is correct by adding UnpaidEMIAmountE and "
                    f"UnpaidPenaltyAmountE::Loan ID::{i}")
            else:

                print(
                    f"Error::Total unpaid amount in EMI data is not correct by adding UnpaidEMIAmountE and "
                    f"UnpaidPenaltyAmountE::Loan ID::{i}")

            # assert sum(totalUnpaidAmountE) == sum(UnpaidEMIAmountE) + sum(UnpaidPenaltyAmountE), "Total unpaid amount in EMI data is correct by adding UnpaidEMIAmountE and UnpaidPenaltyAmountE"

            print("***************************************************************************")
        print("missMatchOfPaid::", missMatchOfPaid)
        print("missMatchOfUnpaid::", missMatchOfUnpaid)

    # 1.Total amount to be paid() = EMI amount(EMI amount) + Penalty amount (Penalty amount)
    # 2.Total paid amount(Total paid amount) = sum (Total paid amount) or equal to (Paid EMI amount)
    # 3.Total unpaid amount(Total unpaid amount) = Total amount to be paid - Total paid amount
