import requests
import json

# sample LIDs:430144,572277,532329




class TestRepayment:
    def test_getRepayment(self):
        # Upcoming EMI


        response = requests.get(
            "https://lendittfinserve.com/prod/admin/loan/getEMIRepaymentDetails",params={"loanId":572277},
            verify=False)    #current date


        # print('status code of get Repayment::', response.status_code)
        # print(response.json())
        sData = response.json()
        jdata = json.dumps(sData,indent=2)
        print(jdata)

        # print(response.headers)
        print(response.content)

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
        PaidEMIAmountE = []
        totalPaidAmountE = []
        paidPenaltyAmountE = []
        totalUnpaidAmountE = []
        UnpaidEMIAmountE = []
        UnpaidPenaltyAmountE = []



        for i in emiData:
            if "EMI date" in i:
                emiDateE.append(i['EMI date'])
                # print(i['EMI date'])

            if "EMI amount" in i:
                emiAmountE.append(i['EMI amount'])

            if "Principal Amount" in i:
                principalAmountE.append(i['Principal Amount'])

            if "Interest Amount" in i:
                interestAmountE.append(i['Interest Amount'])

            if "Penalty days" in i:
                penaltyDaysE.append(i['Penalty days'])

            if "Penalty amount" in i:
                penaltyAmountE.append(i['Penalty amount'])

            if "Paid EMI amount" in i:
                PaidEMIAmountE.append(i['Paid EMI amount'])

            if "Total paid amount" in i:
                totalPaidAmountE.append(i['Total paid amount'])

            if "Paid Penalty amount" in i:
                paidPenaltyAmountE.append(i['Paid Penalty amount'])

            if "Total unpaid amount" in i:
                totalUnpaidAmountE.append(i['Total unpaid amount'])

            if "Unpaid EMI amount" in i:
                UnpaidEMIAmountE.append(i['Unpaid EMI amount'])

            if "Unpaid penalty amount" in i:
                UnpaidPenaltyAmountE.append(i['Unpaid penalty amount'])

            else:
                print("error")

        # print('EMI DATA:>','emiDate::',emiDateE,'emiAmount::',emiAmountE,'principalAmount::',principalAmountE,'interestAmount::',interestAmountE,'penaltyDays::',penaltyDaysE,'penaltyAmount::',penaltyAmountE,'totalPaidAmount::',totalPaidAmountE,'paidPenaltyAmount::',paidPenaltyAmountE,'totalUnpaidAmount::',totalUnpaidAmountE,'UnpaidEMIAmount::',UnpaidEMIAmountE,'UnpaidPenaltyAmount::',UnpaidPenaltyAmountE)

        print("totalPaidAmountE::",sum(totalPaidAmountE))
        print("emiAmountE::", sum(emiAmountE))
        print("totalUnpaidAmountE::", sum(totalUnpaidAmountE))



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


        totalAmountToBePaidAdd = emiAmountE + penaltyAmountE
        totalAmountToBePaidForm = sum(totalAmountToBePaidAdd)
        print("totalAmountToBePaidForm::",totalAmountToBePaidForm)

        totalPaidAmountT = sum(tPaidAmount)
        print("totalPaidAmountTran::",totalPaidAmountT)

        totalUnpaidAmountForm = (totalAmountToBePaidForm - totalPaidAmountT)-1
        print("totalUnpaidAmountForm::",totalUnpaidAmountForm)


        print("totalUnpaidAmountE::", sum(totalUnpaidAmountE))
        print("UnpaidEMIAmountE::", sum(UnpaidEMIAmountE))
        print("UnpaidPenaltyAmountE::", sum(UnpaidPenaltyAmountE))



        if sum(totalPaidAmountE) == totalPaidAmountT:
            print("Total amount paid in EMI data is as per formula")
        else:
            print("Error::Total amount paid in EMI data is not as per formula")


        if sum(totalUnpaidAmountE) == totalUnpaidAmountForm:
            print("Total unpaid amount in EMI data is as per formula")
        else:
            print("Error::Total unpaid amount in EMI data is not as per formula")


        if sum(totalUnpaidAmountE) == sum(UnpaidEMIAmountE) + sum(UnpaidPenaltyAmountE):
            print("Total unpaid amount in EMI data is correct by adding UnpaidEMIAmountE and UnpaidPenaltyAmountE")
        else:
            print("Error::Total unpaid amount in EMI data is not correct by adding UnpaidEMIAmountE and UnpaidPenaltyAmountE")


        assert sum(totalPaidAmountE) == totalPaidAmountT, "Total amount paid in EMI data is as per formula"
        assert sum(totalUnpaidAmountE) == totalUnpaidAmountForm, "Total unpaid amount in EMI data is as per formula"
        assert sum(totalUnpaidAmountE) == sum(UnpaidEMIAmountE) + sum(UnpaidPenaltyAmountE), "Total unpaid amount in EMI data is correct by adding UnpaidEMIAmountE and UnpaidPenaltyAmountE"





#1.Total amount to be paid() = EMI amount(EMI amount) + Penalty amount (Penalty amount)
#2.Total paid amount(Total paid amount) = sum (Total paid amount) or equal to (Paid EMI amount)
#3.Total unpaid amount(Total unpaid amount) = Total amount to be paid - Total paid amount


