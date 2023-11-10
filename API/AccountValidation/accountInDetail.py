import requests


class TestAccount:

    def test_getAllDisb(self):
        '''tally/getAllDisbursementDetails'''
        response1 = requests.get(
            "https://lendittfinserve.com/prod/admin/tally/getAllDisbursementDetails?startDate=2023-09-27T10:00:00.000Z&endDate=2023-09-27T10:00:00.000Z") #

        # '''getting loan id of AutoDebitFail'''

        lATB = response1.json()["data"]["titles"][0]
        lATB_name = response1.json()["data"]["titles"][0]["name"]
        lATB_totalDebit = response1.json()["data"]["titles"][0]["debit"] #value
        lATB_totalDebitComma = lATB_totalDebit[1:]
        lATB_totalDebitFloat = float(lATB_totalDebitComma.replace(",", ""))
        print("lATB_totalDebitFloat::", lATB_totalDebitFloat)

        lATB_totalCredit = response1.json()["data"]["titles"][0]["credit"]

        cTB = response1.json()["data"]["titles"][1]
        cTBTotalName = response1.json()["data"]["titles"][1]["name"]
        cTBTotalCredit = response1.json()["data"]["titles"][1]["credit"]
        cTBTotalDebit = response1.json()["data"]["titles"][1]["debit"]
        cTBProssFeesName = response1.json()["data"]["titles"][1]["subtitles"][0]["name"]
        cTBProssFeesCredit = response1.json()["data"]["titles"][1]["subtitles"][0]["credit"]
        cTBProssFeesDebit = response1.json()["data"]["titles"][1]["subtitles"][0]["debit"]

        cTBStampDuty = response1.json()["data"]["titles"][1]["subtitles"][1]
        cTBStampDutyName = response1.json()["data"]["titles"][1]["subtitles"][1]["name"]
        cTBStampDutyCredit = response1.json()["data"]["titles"][1]["subtitles"][1]["credit"]
        cTBStampDutyDebit = response1.json()["data"]["titles"][1]["subtitles"][1]["debit"]

        # OnlConvFees
        cTBOnlConvFees = response1.json()["data"]["titles"][1]["subtitles"][2]
        cTBOnlConvFeesName = response1.json()["data"]["titles"][1]["subtitles"][2]["name"]
        cTBOnlConvFeesCredit = response1.json()["data"]["titles"][1]["subtitles"][2]["credit"]
        cTBOnlConvFeesDebit = response1.json()["data"]["titles"][1]["subtitles"][2]["debit"]

        #DocuCharge
        cTBDocuCharge = response1.json()["data"]["titles"][1]["subtitles"][3]
        cTBDocuChargeName = response1.json()["data"]["titles"][1]["subtitles"][3]["name"]
        cTBDocuChargeCredit = response1.json()["data"]["titles"][1]["subtitles"][3]["credit"]
        cTBDocuChargeDebit = response1.json()["data"]["titles"][1]["subtitles"][3]["debit"]

        cTB_SGST = response1.json()["data"]["titles"][1]["subtitles"][4]
        cTB_SGSTName = response1.json()["data"]["titles"][1]["subtitles"][4]["name"]
        cTB_SGSTCredit = response1.json()["data"]["titles"][1]["subtitles"][4]["credit"]
        cTB_SGSTDebit = response1.json()["data"]["titles"][1]["subtitles"][4]["debit"]

        cTB_CGST = response1.json()["data"]["titles"][1]["subtitles"][5]
        cTB_CGSTName = response1.json()["data"]["titles"][1]["subtitles"][5]["name"]
        cTB_CGSTCredit = response1.json()["data"]["titles"][1]["subtitles"][5]["credit"]
        cTB_CGSTDebit = response1.json()["data"]["titles"][1]["subtitles"][5]["debit"]

        cTB_InsuCharg = response1.json()["data"]["titles"][1]["subtitles"][6]
        cTB_InsuChargName = response1.json()["data"]["titles"][1]["subtitles"][6]["name"]
        cTB_InsuChargCredit = response1.json()["data"]["titles"][1]["subtitles"][6]["credit"]
        cTB_InsuChargDebit = response1.json()["data"]["titles"][1]["subtitles"][6]["debit"]


        #DISBURSED AMOUNT TO BORROWER
        disbAmtTOBorr = response1.json()["data"]["titles"][2]["credit"]

        # TOTAL AMOUNT
        totalAmountCredit = response1.json()["data"]["titles"][3]["credit"]


        total_loans = response1.json()["data"]["totalLoan"]
        print("total_loans::",total_loans)


        lATB = response1.json()["data"]["titles"][2]
        lATB = response1.json()["data"]["titles"][3]

        # print('status code of get Upcoming EMI::', response1.status_code)
        # print(response1.json())

        #
        lATB_totalDebitComma = lATB_totalDebit[1:]
        lATB_totalDebitInt = int(lATB_totalDebitComma.replace(",",""))
        print("lATB_totalDebitInt::",lATB_totalDebitInt)

        # # PROCESSING FEES
        cTBProssFeesCreditComma = cTBProssFeesCredit[1:]
        cTBProssFeesCreditFloat = float(cTBProssFeesCreditComma.replace(",", ""))
        print("cTBProssFeesCreditInt::",cTBProssFeesCreditFloat)
        #
        # processFessForm = (float(lATB_totalDebitInt) * 0.065)
        # print("processFessForm::", processFessForm)
        #

        # if cTBProssFeesCreditFloat == processFessForm:
        #     print("CHARGES TO BORROWER credit is as per formula")
        # else:
        #     print("Error::CHARGES TO BORROWER credit is not as per formula")
        #
        # assert cTBProssFeesCreditFloat == processFessForm, "CHARGES TO BORROWER credit is as per formula"



        # # STAMP DUTY
        cTBStampDutyCreditComma = cTBStampDutyCredit[1:]
        cTBStampDutyCreditFloat = float(cTBStampDutyCreditComma.replace(",", ""))
        print("cTBStampDutyCreditInt::",cTBStampDutyCreditFloat)
        #
        # stampDutyForm = float(total_loans) * 300
        # print("stampDutyForm::", stampDutyForm)
        #
        # if cTBStampDutyCreditFloat == stampDutyForm:
        #     print("CHARGES TO BORROWER stamp duty is as per formula")
        # else:
        #     print("Error::CHARGES TO BORROWER stamp duty is not as per formula")
        #
        # assert cTBStampDutyCreditFloat == stampDutyForm, "CHARGES TO BORROWER stamp duty is as per formula"


        # # ONLINE CONVINENCE FEES
        cTBOnlConvFeesCreditComma = cTBOnlConvFeesCredit[1:]
        cTBOnlConvFeesCreditFloat = float(cTBOnlConvFeesCreditComma.replace(",", ""))
        print("cTBOnlConvFeesCreditFloat::", cTBOnlConvFeesCreditFloat)
        #
        # onlConvFeesForm = float(total_loans) * 150
        # print("onlConvFeesForm::", onlConvFeesForm)
        #
        # if cTBOnlConvFeesCreditFloat == onlConvFeesForm:
        #     print("CHARGES TO BORROWER online convenience fees is as per formula")
        # else:
        #     print("Error::CHARGES TO BORROWER online convenience fees is not as per formula")
        #
        # assert cTBOnlConvFeesCreditFloat == onlConvFeesForm, "CHARGES TO BORROWER online convenience fees is as per formula"


        # #DOCUMENT CHARGES
        cTBDocuChargeCreditComma = cTBDocuChargeCredit[1:]
        cTBDocuChargeCreditFloat = float(cTBDocuChargeCreditComma.replace(",", ""))
        print("cTBDocuChargeCreditFloat::", cTBDocuChargeCreditFloat)
        #
        # docuChargForm = float(lATB_totalDebitFloat) * 0.01
        # print("docuChargForm::",docuChargForm)
        #
        # if cTBDocuChargeCreditFloat == docuChargForm:
        #     print("CHARGES TO BORROWER document charges is as per formula")
        # else:
        #     print("Error::CHARGES TO BORROWER document charges is not as per formula")
        #
        # assert cTBDocuChargeCreditFloat == docuChargForm, "CHARGES TO BORROWER document charges is as per formula"


        # # SGST(9%)
        cTBSGSTComma = cTB_SGSTCredit[1:]
        cTBSGSTFloat = round(float(cTBSGSTComma.replace(",", "")))
        print("cTBSGSTFloat::", cTBSGSTFloat)
        #
        # SGSTForm = round(float(cTBProssFeesCreditFloat+cTBOnlConvFeesCreditFloat+cTBDocuChargeCreditFloat) * 0.09)
        # print("SGSTForm::",SGSTForm)
        #
        # if cTBSGSTFloat == SGSTForm:
        #     print("CHARGES TO BORROWER SGST is as per formula")
        # else:
        #     print("Error::CHARGES TO BORROWER SGST is not as per formula")
        #
        # assert cTBSGSTFloat == SGSTForm, "CHARGES TO BORROWER SGST is as per formula"



        #
        # # CGST(9%)
        cTBCGSTComma = cTB_CGSTCredit[1:]
        cTBCGSTFloat = float(cTBCGSTComma.replace(",", ""))
        print("cTBCGSTFloat::", cTBCGSTFloat)
        #
        # CGSTForm = round(float(cTBProssFeesCreditFloat+cTBOnlConvFeesCreditFloat+cTBDocuChargeCreditFloat) * 0.09,2)
        # print("CGSTForm::",CGSTForm)
        #
        # if round(cTBCGSTFloat) == round(CGSTForm):
        #     print("CHARGES TO BORROWER CGST is as per formula")
        # else:
        #     print("Error::CHARGES TO BORROWER CGST is not as per formula")
        #
        # assert cTBCGSTFloat == CGSTForm, "CHARGES TO BORROWER CGST is as per formula"



       #  # INSURANCE CHARGES
        cTB_InsuChargCreditComma = cTB_InsuChargCredit[1:]
        cTB_InsuChargCreditFloat = float(cTB_InsuChargCreditComma.replace(",", ""))
        print("cTB_InsuChargCreditFloat::", cTB_InsuChargCreditFloat)
       #
       #  allDisbursedLoansAPI =  requests.get(
       #      "https://lendittfinserve.com/prod/admin/dashboard/allDisbursedLoans?start_date=2023-09-27T10%3A00%3A00.000Z&end_date=2023-09-27T10%3A00%3A00.000Z&page=1&download=true") #
       #
       #
       # ## print('status code of get DisbursedLoans::', allDisbursedLoansAPI.status_code)
       #  ## print(allDisbursedLoansAPI.json())
       #
       #  allDisbLoans = allDisbursedLoansAPI.json()["data"]["rows"]
       #
       #  insurPrem = []
       #  #
       #  for dl in allDisbLoans:
       #      if "Insurance premium" in dl:
       #          if type(dl["Insurance premium"]) == (int or float):
       #              insurPrem.append(dl["Insurance premium"])
       #
       #  print(insurPrem)
       #
       #  insurPremTotal = round(sum(insurPrem), 2)
       #  print("insurPremTotal::", insurPremTotal)
       #  # #
       #  print("cTB_InsuChargCreditFloat::",cTB_InsuChargCreditFloat)
       #
       #  cTB_InsuChargCreditInt = round(cTB_InsuChargCreditFloat) + 1
       #  print("cTB_InsuChargCreditInt::", cTB_InsuChargCreditInt)
       #  #
       #
       #  if cTB_InsuChargCreditInt == insurPremTotal:
       #      print("cTB_InsuChargCreditInt matched with insurPremTotal")
       #  else:
       #      print("Error::cTB_InsuChargCreditInt not matched with insurPremTotal in allDisbursedLoans API")
       #
       #  assert cTB_InsuChargCreditInt == insurPremTotal


        #TOTAL CHARGES TO BORROWER by adding all charges
        totalChargOfChToBorrElem = cTBProssFeesCreditFloat + cTBStampDutyCreditFloat + cTBOnlConvFeesCreditFloat + cTBDocuChargeCreditFloat + cTBSGSTFloat + cTBCGSTFloat + cTB_InsuChargCreditFloat
        print("totalChargOfChToBorrElem::",totalChargOfChToBorrElem)
        print("cTBTotalCredit::", cTBTotalCredit)

        cTBTotalCreditComma = cTBTotalCredit[1:]
        cTBTotalCreditFloat = float(cTBTotalCreditComma.replace(",", ""))
        # print("cTBTotalCreditFloat::", cTBTotalCreditFloat)



        if round(cTBTotalCreditFloat) == round(totalChargOfChToBorrElem):
            print("cTBTotalCreditFloat matched with totalChargOfChToBorrElem")
        else:
            print("Error::cTBTotalCreditFloat not matched with totalChargOfChToBorrElem")

        assert round(cTBTotalCreditFloat) == round(totalChargOfChToBorrElem)



        # DISBURSED AMOUNT TO BORROWER
        disbAmtTOBorrComma = disbAmtTOBorr[1:]
        disbAmtTOBorrFloat = float(disbAmtTOBorrComma.replace(",", ""))
        print("disbAmtTOBorrFloat::", disbAmtTOBorrFloat)

        total = lATB_totalDebitFloat-cTBTotalCreditFloat
        print("total::", total)

        if (round(lATB_totalDebitFloat) - round(cTBTotalCreditFloat)) == round(disbAmtTOBorrFloat):
            print("Substraction of lATB_totalDebitFloat and cTBTotalCreditTotalFloat matched with disbAmtTOBorrFloat")
        else:
            print("Error::Substraction of lATB_totalDebitFloat and cTBTotalCreditTotalFloat not matched with disbAmtTOBorrFloat")

        assert (round(lATB_totalDebitFloat) - round(cTBTotalCreditFloat)) == round(disbAmtTOBorrFloat)



       #TOTAL AMOUNT
        totalAmountCreditComma = totalAmountCredit[1:]
        totalAmountCreditFloat = float(totalAmountCreditComma.replace(",", ""))
        print("totalAmountCreditFloat::", totalAmountCreditFloat)

        if round(cTBTotalCreditFloat) + round(disbAmtTOBorrFloat) == round(totalAmountCreditFloat):
            print("Addition of cTBTotalCreditFloat and cTBTotalCreditFloat matched with totalAmountCreditFloat")
        else:
            print("Error::Addition of cTBTotalCreditFloat and cTBTotalCreditFloat not matched with totalAmountCreditFloat")

        assert round(cTBTotalCreditFloat) + round(disbAmtTOBorrFloat) == round(totalAmountCreditFloat)






        # ##REPAYMENT SUMMARY
        # response2 = requests.get(
        #     "https://lendittfinserve.com/prod/admin/tally/getAllRepaymentData?startDate=2023-09-26T10:00:00.000Z&endDate=2023-09-26T10:00:00.000Z")  #
        #
        # '''getting tally/getAllRepaymentData'''
        #
        #
        #
        # # print('status code of get tally/getAllRepaymentData::', response2.status_code)
        # # print(response2.json())
        #
        #
        # # TOTAL REPAID AMOUNT FROM BORROWER
        # total_loans = response2.json()["data"]["totalLoan"]
        # print("total_loans in repayment::",total_loans)
        # tRepaidAmountFromBorrower = response2.json()["data"]["titles"][0]
        # tRepaidAmountFromBorrowerName = response2.json()["data"]["titles"][0]["name"]
        # tRepaidAmountFromBorrowerDebitTotal = response2.json()["data"]["titles"][0]["debit"]
        # tRepaidAmountFromBorrowerCreditTotal = response2.json()["data"]["titles"][0]["credit"]
        #
        # tRepaidAmountFromBorrowerCreditPrincipleName = response2.json()["data"]["titles"][0]["subtitles"][0]["name"]
        # tRepaidAmountFromBorrowerCreditPDebitPrincipleDebit = response2.json()["data"]["titles"][0]["subtitles"][1]["debit"]
        # tRepaidAmountFromBorrowerCreditCreditPrincipleCredit = response2.json()["data"]["titles"][0]["subtitles"][2]["credit"]
        #
        #
        # tRepaidAmountFromBorrowerCreditInterestName = response2.json()["data"]["titles"][0]["subtitles"][1]["name"]
        # tRepaidAmountFromBorrowerCreditInterestDebit = response2.json()["data"]["titles"][0]["subtitles"][1]["debit"]
        # tRepaidAmountFromBorrowerCreditInterestCredit = response2.json()["data"]["titles"][0]["subtitles"][1]["credit"]
        #
        #
        # tRepaidAmountFromBorrowerCreditPenaltyName = response2.json()["data"]["titles"][0]["subtitles"][2]["name"]
        # tRepaidAmountFromBorrowerCreditPenaltyDebit = response2.json()["data"]["titles"][0]["subtitles"][2]["debit"]
        # tRepaidAmountFromBorrowerCreditPenaltyCredit = response2.json()["data"]["titles"][0]["subtitles"][2]["credit"]
        #
        #
        # tRepaidAmountFromBorrowerCreditRoundOfffName = response2.json()["data"]["titles"][0]["subtitles"][3]["name"]
        # tRepaidAmountFromBorrowerCreditRoundOffDebit = response2.json()["data"]["titles"][0]["subtitles"][3]["debit"]
        # tRepaidAmountFromBorrowerCreditRoundOffCredit = response2.json()["data"]["titles"][0]["subtitles"][3]["credit"]
        #
        # #AMOUNT RECIEVED IN
        # amountReceivedInName = response2.json()["data"]["titles"][1]["name"]
        # amountReceivedInDebitTotal = response2.json()["data"]["titles"][1]["debit"]
        # amountReceivedInCreditTotal = response2.json()["data"]["titles"][1]["credit"]
        # #RAZORPAY-1
        # amountReceivedInSubtitles= response2.json()["data"]["titles"][1]["subtitles"]
        # amountReceivedInRazorpay1Name = response2.json()["data"]["titles"][1]["subtitles"][0]["name"]
        # amountReceivedInRazorpay1Debit = response2.json()["data"]["titles"][1]["subtitles"][0]["debit"]
        # amountReceivedInRazorpay1Credit = response2.json()["data"]["titles"][1]["subtitles"][0]["credit"]
        # #RAZORPAY-2
        # amountReceivedInSubtitles = response2.json()["data"]["titles"][1]["subtitles"]
        # amountReceivedInRazorpay2Name = response2.json()["data"]["titles"][1]["subtitles"][1]["name"]
        # amountReceivedInRazorpay2Debit = response2.json()["data"]["titles"][1]["subtitles"][1]["debit"]
        # amountReceivedInRazorpay2Credit = response2.json()["data"]["titles"][1]["subtitles"][1]["credit"]
        #
        # #CASHFREE
        # amountReceivedInSubtitles = response2.json()["data"]["titles"][1]["subtitles"]
        # amountReceivedInCashFreeName = response2.json()["data"]["titles"][1]["subtitles"][2]["name"]
        # amountReceivedInCashFreeDebit = response2.json()["data"]["titles"][1]["subtitles"][2]["debit"]
        # amountReceivedInCashFreeCredit = response2.json()["data"]["titles"][1]["subtitles"][2]["credit"]
        #
        # #bank transfer
        # amountReceivedInSubtitles = response2.json()["data"]["titles"][1]["subtitles"]
        # amountReceivedIn_bankTransferName = response2.json()["data"]["titles"][1]["subtitles"][3]["name"]
        # amountReceivedIn_bankTransferDebit = response2.json()["data"]["titles"][1]["subtitles"][3]["debit"]
        # amountReceivedIn_bankTransferCredit = response2.json()["data"]["titles"][1]["subtitles"][3]["credit"]
        #
        # #TOTAL NET IN-FLOW
        # totalNetInflowName = response2.json()["data"]["titles"][2]["name"]
        # totalNetInflowDebit = response2.json()["data"]["titles"][2]["debit"]
        # totalNetInflowCredit = response2.json()["data"]["titles"][2]["credit"]




        # WALLET SETTLEMENT


        # response3 = requests.get(
        #     "https://lendittfinserve.com/prod/admin/tally/getWalletSettlementDetails?startDate=2023-09-25T10%3A00%3A00.000Z&endDate=2023-09-25T10%3A00%3A00.000Z")  #

        # '''getting tally/getWalletSettlementDetails'''

        # print('status code of get Upcoming EMI::', response3.status_code)
        # print(response3.json())

        #
        # #RAZORPAY-1
        # walletRaz1NameTotal = response3.json()["data"]["titles"][0]["name"]
        # walletRaz1DebitTotal = response3.json()["data"]["titles"][0]["debit"]
        # walletRaz1CreditTotal = response3.json()["data"]["titles"][0]["credit"]
        #
        #
        # #RAZORPAY SETTLEMENT
        # walletRaz1Settl = response3.json()["data"]["titles"][0]["subtitles"]
        # walletRaz1SettlName = response3.json()["data"]["titles"][0]["subtitles"][0]["name"]
        # walletRaz1SettlDebit = response3.json()["data"]["titles"][0]["subtitles"][0]["debit"]
        # walletRaz1SettlCredit = response3.json()["data"]["titles"][0]["subtitles"][0]["credit"]
        #
        # #RAZORPAY GST
        # walletRaz1GST = response3.json()["data"]["titles"][0]["subtitles"]
        # walletRaz1GSTName = response3.json()["data"]["titles"][0]["subtitles"][1]["name"]
        # walletRaz1GSTDebit = response3.json()["data"]["titles"][0]["subtitles"][1]["debit"]
        # walletRaz1GSTCredit = response3.json()["data"]["titles"][0]["subtitles"][1]["credit"]
        #
        # #RAZORPAY CHARGES
        # walletRaz1Charg = response3.json()["data"]["titles"][0]["subtitles"]
        # walletRaz1ChargName = response3.json()["data"]["titles"][0]["subtitles"][2]["name"]
        # walletRaz1ChargDebit = response3.json()["data"]["titles"][0]["subtitles"][2]["debit"]
        # walletRaz1ChargCredit = response3.json()["data"]["titles"][0]["subtitles"][2]["credit"]
        #
        # #AMOUNT RECIEVED IN
        # amtReceivedInRaz1Name = response3.json()["data"]["titles"][0]["subtitles"][3]["name"]
        # amtReceivedInRaz1Debit = response3.json()["data"]["titles"][0]["subtitles"][3]["debit"]
        # amtReceivedInRaz1Credit = response3.json()["data"]["titles"][0]["subtitles"][3]["credit"]
        #
        # #ICICI BANK - 30400
        # amtReceivedInRaz1ICICI30400Name = response3.json()["data"]["titles"][0]["subtitles"][3]["section"][0]["name"]
        # amtReceivedInRaz1ICICI30400Debit = response3.json()["data"]["titles"][0]["subtitles"][3]["section"][0]["debit"]
        # amtReceivedInRaz1ICICI30400Credit = response3.json()["data"]["titles"][0]["subtitles"][3]["section"][0]["credit"]
        #
        # #ICICI BANK - 753
        # amtReceivedInRaz1ICICI753Name = response3.json()["data"]["titles"][0]["subtitles"][3]["section"][1]["name"]
        # amtReceivedInRaz1ICICI753Debit = response3.json()["data"]["titles"][0]["subtitles"][3]["section"][1]["debit"]
        # amtReceivedInRaz1ICICI753Credit = response3.json()["data"]["titles"][0]["subtitles"][3]["section"][1]["credit"]
        #
        # #RBL BANK
        # amtReceivedInRaz1RBLBankName = response3.json()["data"]["titles"][0]["subtitles"][3]["section"][2]["name"]
        # amtReceivedInRaz1RBLBankDebit = response3.json()["data"]["titles"][0]["subtitles"][3]["section"][2]["debit"]
        # amtReceivedInRaz1RBLBankCredit = response3.json()["data"]["titles"][0]["subtitles"][3]["section"][2]["credit"]
        #
        #




        #
        # #RAZORPAY-2
        # walletRaz2Name = response3.json()["data"]["titles"][1]["name"]
        # walletRaz2DebitTotal = response3.json()["data"]["titles"][1]["debit"]
        # walletRaz2CreditTotal = response3.json()["data"]["titles"][1]["credit"]
        #
        #
        # #RAZORPAY SETTLEMENT
        # walletRaz2Settl = response3.json()["data"]["titles"][1]["subtitles"]
        # walletRaz2SettlName = response3.json()["data"]["titles"][1]["subtitles"][0]["name"]
        # walletRaz2SettlDebit = response3.json()["data"]["titles"][1]["subtitles"][0]["debit"]
        # walletRaz2SettlCredit = response3.json()["data"]["titles"][1]["subtitles"][0]["credit"]
        #
        # # #RAZORPAY GST
        # walletRaz2GST = response3.json()["data"]["titles"][1]["subtitles"]
        # walletRazGSTName = response3.json()["data"]["titles"][1]["subtitles"][1]["name"]
        # walletRazGSTDebit = response3.json()["data"]["titles"][1]["subtitles"][1]["debit"]
        # walletRaz2GSTCredit2 = response3.json()["data"]["titles"][1]["subtitles"][1]["credit"]
        # #
        # # #RAZORPAY CHARGES
        # walletRaz2Charg = response3.json()["data"]["titles"][1]["subtitles"]
        # walletRaz2ChargName = response3.json()["data"]["titles"][1]["subtitles"][2]["name"]
        # walletRaz2ChargDebit = response3.json()["data"]["titles"][1]["subtitles"][2]["debit"]
        # walletRaz2ChargCredit = response3.json()["data"]["titles"][1]["subtitles"][2]["credit"]
        # #
        # # #AMOUNT RECIEVED IN Raz2
        # amtReceivedInRaz2Name = response3.json()["data"]["titles"][1]["subtitles"][3]["name"]
        # amtReceivedInRaz2Debit = response3.json()["data"]["titles"][1]["subtitles"][3]["debit"]
        # amtReceivedInRaz2Credit = response3.json()["data"]["titles"][1]["subtitles"][3]["credit"]
        # #
        # # #ICICI BANK - 30400
        # amtReceivedInRaz2ICICI30400Name = response3.json()["data"]["titles"][1]["subtitles"][3]["section"][0]["name"]
        # amtReceivedInRaz2ICICI30400Debit = response3.json()["data"]["titles"][1]["subtitles"][3]["section"][0]["debit"]
        # amtReceivedInRaz2ICICI30400Credit = response3.json()["data"]["titles"][1]["subtitles"][3]["section"][0]["credit"]
        # #
        # # #ICICI BANK - 753
        # amtReceivedInRaz2ICICI753Name = response3.json()["data"]["titles"][1]["subtitles"][3]["section"][1]["name"]
        # amtReceivedInRaz2ICICI753Debit = response3.json()["data"]["titles"][1]["subtitles"][3]["section"][1]["debit"]
        # amtReceivedInRaz2ICICI753Credit = response3.json()["data"]["titles"][1]["subtitles"][3]["section"][1]["credit"]
        #
        # # #RBL BANK
        # amtReceivedInRaz2RBLBankName = response3.json()["data"]["titles"][1]["subtitles"][3]["section"][2]["name"]
        # amtReceivedInRaz2RBLBankDebit = response3.json()["data"]["titles"][1]["subtitles"][3]["section"][2]["debit"]
        # amtReceivedInRaz2RBLBankCredit = response3.json()["data"]["titles"][1]["subtitles"][3]["section"][2]["credit"]
        #

        # #CASHFREE
        #
        # walletCashFreeName = response3.json()["data"]["titles"][2]["name"]
        # walletCashFreeDebitTotal = response3.json()["data"]["titles"][2]["debit"]
        # walletCashFreeCreditTotal = response3.json()["data"]["titles"][2]["credit"]
        #
        #
        # #CASHFREE SETTLEMENT
        # walletCashFreeSettl = response3.json()["data"]["titles"][2]["subtitles"]
        # walletCashFreeSettlName = response3.json()["data"]["titles"][2]["subtitles"][0]["name"]
        # walletCashFreeSettlDebit = response3.json()["data"]["titles"][2]["subtitles"][0]["debit"]
        # walletCashFreeSettlCredit = response3.json()["data"]["titles"][2]["subtitles"][0]["credit"]
        #
        # # #CASHFREE  GST
        # walletCashFreeGST = response3.json()["data"]["titles"][2]["subtitles"]
        # walletCashFreeGSTName = response3.json()["data"]["titles"][2]["subtitles"][1]["name"]
        # walletCashFreeGSTDebit = response3.json()["data"]["titles"][2]["subtitles"][1]["debit"]
        # walletCashFreeGSTCredit = response3.json()["data"]["titles"][2]["subtitles"][1]["credit"]
        #
        # # # #CASHFREE  CHARGES
        # walletCashFreeCharg = response3.json()["data"]["titles"][2]["subtitles"]
        # walletCashFreeChargName = response3.json()["data"]["titles"][2]["subtitles"][2]["name"]
        # walletCashFreeChargDebit = response3.json()["data"]["titles"][2]["subtitles"][2]["debit"]
        # walletCashFreeChargCredit = response3.json()["data"]["titles"][2]["subtitles"][2]["credit"]
        #
        #
        # # #CASHFREE REFUND
        # walletCashFreeRefundName = response3.json()["data"]["titles"][2]["subtitles"][3]["name"]
        # walletCashFreeRefundDebit = response3.json()["data"]["titles"][2]["subtitles"][3]["debit"]
        # walletCashFreeRefundCredit = response3.json()["data"]["titles"][2]["subtitles"][3]["credit"]
        #
        #
        # # # #AMOUNT RECIEVED IN CASHFREE
        # amtReceivedInCashFreeName = response3.json()["data"]["titles"][2]["subtitles"][4]["name"]
        # amtReceivedInCashFreeDebitTotal = response3.json()["data"]["titles"][2]["subtitles"][4]["debit"]
        # amtReceivedInCashFreeCreditTotal = response3.json()["data"]["titles"][2]["subtitles"][4]["credit"]
        # #
        #
        # # # #ICICI BANK - 30400
        # amtReceivedInICICI30400CashFreeName = response3.json()["data"]["titles"][2]["subtitles"][4]["section"][0]["name"]
        # amtReceivedInICICI30400CashFreeDebit = response3.json()["data"]["titles"][2]["subtitles"][4]["section"][0]["debit"]
        # amtReceivedInICICI30400CashFreeCredit = response3.json()["data"]["titles"][2]["subtitles"][4]["section"][0]["credit"]
        # # #
        # # # #ICICI BANK - 753
        # amtReceivedInICICI753CashFreeName = response3.json()["data"]["titles"][2]["subtitles"][4]["section"][1]["name"]
        # amtReceivedInICICI753CashFreeDebit = response3.json()["data"]["titles"][2]["subtitles"][4]["section"][1]["debit"]
        # amtReceivedInICICI753CashFreeCredit = response3.json()["data"]["titles"][2]["subtitles"][4]["section"][1]["credit"]
        # #
        # # # #RBL BANK
        # amtReceivedInRBLBankCashFreeName = response3.json()["data"]["titles"][2]["subtitles"][4]["section"][2]["name"]
        # amtReceivedInRBLBankCashFreeDebit = response3.json()["data"]["titles"][2]["subtitles"][4]["section"][2]["debit"]
        # amtReceivedInRBLBankCashFreeCredit = response3.json()["data"]["titles"][2]["subtitles"][4]["section"][2]["credit"]
        #
        # #Total of wallet settlement
        # TotalOfWalletSettlementName = response3.json()["data"]["titles"][3]["name"]
        # TotalOfWalletSettlementDebit = response3.json()["data"]["titles"][3]["debit"]
        # TotalOfWalletSettlementCredit = response3.json()["data"]["titles"][3]["credit"]
        #
        #
        # #EXPENSES ON ACCOUNT OF REFERRAL
        # ExpensesOnAccountReferDebit = response3.json()["data"]["expenseReferral"]["debit"]
        # ExpensesOnAccountReferCredit = response3.json()["data"]["expenseReferral"]["credit"]
        #
        #




        # print(TotalOfWalletSettlementName)
        # print(TotalOfWalletSettlementDebit)
        # print(TotalOfWalletSettlementCredit)



        # # AllRepaidLoans
        # response4 = requests.get(
        #     "https://lendittfinserve.com/prod/admin/transaction/allRepaidLoans?start_date=2023-09-26T10:00:00.000Z&end_date=2023-09-26T10:00:00.000Z&page=1&pagesize=10&getTotal=true&download=true")  #
        #
        # # '''getting transaction/allRepaidLoans'''
        #
        # # print('status code of get Upcoming EMI::', response4.status_code)
        # # print(response4.json())
        #
        #
        # allTransRepay = response4.json()["data"]["rows"]
        #
        # # print(allTransRepay)
        #
        # repaidAmt = []
        #
        # for rd in allTransRepay:
        #     if "Repaid amount" in rd:
        #         repaidAmt.append(rd["Repaid amount"])
        #
        #
        #
        # # print(repaidAmt)
        # totalRepayTransAmt = round(sum(repaidAmt),2)
        # print("totalRepayTransAmt::",totalRepayTransAmt)
        #
        # # print("tRepaidAmountFromBorrowerCreditTotal::",tRepaidAmountFromBorrowerCreditTotal)
        #
        # tRepaidAmountFromBorrowerCreditTotalComma = tRepaidAmountFromBorrowerCreditTotal[1:]
        # tRepaidAmountFromBorrowerCreditTotalFloat = round(float(tRepaidAmountFromBorrowerCreditTotalComma.replace(",", "")),2)
        # print("tRepaidAmountFromBorrowerCreditTotalFloat::",tRepaidAmountFromBorrowerCreditTotalFloat)
        #
        # if totalRepayTransAmt == tRepaidAmountFromBorrowerCreditTotalFloat:
        #     print("totalRepayTransAmt matched with tRepaidAmountFromBorrowerCreditTotalFloat")
        # else:
        #     print("Error::totalRepayTransAmt not matched with tRepaidAmountFromBorrowerCreditTotalFloat")
        #
        # assert totalRepayTransAmt == tRepaidAmountFromBorrowerCreditTotalFloat




        # #AllDisbursedLoans
        # response5 = requests.get(
        #     "https://lendittfinserve.com/prod/admin/dashboard/allDisbursedLoans?start_date=2023-09-26T10%3A00%3A00.000Z&end_date=2023-09-26T10%3A00%3A00.000Z&page=1&download=true")  #
        #
        # # '''getting transaction/allDisbursedLoans'''
        #
        # # print('status code of get DisbursedLoans::', response5.status_code)
        # # print(response5.json())
        #
        # allDisbursedLoans = response5.json()["data"]["rows"]
        # #
        # # print(allDisbursedLoans)
        # #
        # approvedAmt = []
        # #
        # for ea in allDisbursedLoans:
        #     if "Approved amount" in ea:
        #         approvedAmt.append(ea["Approved amount"])
        # #
        # print(approvedAmt)
        # approvedAmtTotal = round(sum(approvedAmt), 2)
        # print("approvedAmtTotal::", approvedAmtTotal)
        # #
        # print("lATB_totalDebitInt::",lATB_totalDebitInt)
        #
        # lATB_totalDebitIntComma = lATB_totalDebitInt[1:]
        # lATB_totalDebitIntFloat = round(float(lATB_totalDebitIntComma.replace(",", "")), 2)
        # print("lATB_totalDebitIntFloat::", lATB_totalDebitIntFloat)
        #
        # if approvedAmtTotal == lATB_totalDebitInt:
        #     print("approvedAmtTotal matched with lATB_totalDebitInt")
        # else:
        #     print("Error::approvedAmtTotal not matched with lATB_totalDebitInt")
        #
        # assert approvedAmtTotal == lATB_totalDebitInt





