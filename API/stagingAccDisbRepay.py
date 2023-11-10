import pytest
import requests


class TestAccount:
    @pytest.fixture
    def url(self):
        global response1, response2, response5, response4
        response1 = requests.get(
            "https://lendittfinserve.com/prod/admin/tally/getAllDisbursementDetails?startDate=2023-10-06T10:00:00.000Z&endDate=2023-10-06T10:00:00.000Z")  # Current date

        ##REPAYMENT SUMMARY
        response2 = requests.get(
            "https://lendittfinserve.com/prod/admin/tally/getAllRepaymentData?startDate=2023-10-06T10:00:00.000Z&endDate=2023-10-06T10:00:00.000Z")  # current date

        # AllDisbursedLoans
        response5 = requests.get(
            "https://lendittfinserve.com/prod/admin/dashboard/allDisbursedLoans?start_date=2023-10-06T10%3A00%3A00.000Z&end_date=2023-10-06T10%3A00%3A00.000Z&page=1&download=true")  # current date

        # AllRepaidLoans
        response4 = requests.get(
            "https://lendittfinserve.com/prod/admin/transaction/allRepaidLoans?start_date=2023-10-06T10:00:00.000Z&end_date=2023-10-06T10:00:00.000Z&page=1&pagesize=10&getTotal=true&download=true")  # current date

    def test_getDisbSummary(self, url):
        global disbAmtTOBorr, disbAmtTOBorrFloat, lATB_totalDebitFloat, cTBTotalCreditFloat, totalAmountCredit, cTBTotalCreditFloat, lATB_totalDebitInt
        '''tally/getAllDisbursementDetails'''

        # '''DISBURSEMENT SUMMARY'''

        lATB = response1.json()["data"]["titles"][0]
        lATB_name = response1.json()["data"]["titles"][0]["name"]
        lATB_totalDebit = response1.json()["data"]["titles"][0]["debit"]  # value
        lATB_totalDebitComma = lATB_totalDebit[1:]
        lATB_totalDebitFloat = float(lATB_totalDebitComma.replace(",", ""))
        ## print("lATB_totalDebitFloat::", lATB_totalDebitFloat)

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

        # DocuCharge
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

        # DISBURSED AMOUNT TO BORROWER
        disbAmtTOBorr = response1.json()["data"]["titles"][2]["credit"]

        # TOTAL AMOUNT
        totalAmountCredit = response1.json()["data"]["titles"][3]["credit"]

        total_loans = response1.json()["data"]["totalLoan"]
        print("total_loans in disbursement::", total_loans)

        lATB = response1.json()["data"]["titles"][2]
        lATB = response1.json()["data"]["titles"][3]

        # print('status code of get Upcoming EMI::', response1.status_code)
        # print(response1.json())

        lATB_totalDebitComma = lATB_totalDebit[1:]
        lATB_totalDebitInt = int(lATB_totalDebitComma.replace(",", ""))
        ## print("lATB_totalDebitInt::",lATB_totalDebitInt)

        # # PROCESSING FEES
        cTBProssFeesCreditComma = cTBProssFeesCredit[1:]
        cTBProssFeesCreditFloat = float(cTBProssFeesCreditComma.replace(",", ""))
        ## print("cTBProssFeesCreditInt::",cTBProssFeesCreditFloat)

        # # STAMP DUTY
        cTBStampDutyCreditComma = cTBStampDutyCredit[1:]
        cTBStampDutyCreditFloat = float(cTBStampDutyCreditComma.replace(",", ""))
        ## print("cTBStampDutyCreditInt::",cTBStampDutyCreditFloat)

        # # ONLINE CONVINENCE FEES
        cTBOnlConvFeesCreditComma = cTBOnlConvFeesCredit[1:]
        cTBOnlConvFeesCreditFloat = float(cTBOnlConvFeesCreditComma.replace(",", ""))
        ## print("cTBOnlConvFeesCreditFloat::", cTBOnlConvFeesCreditFloat)
        #
        # #DOCUMENT CHARGES
        cTBDocuChargeCreditComma = cTBDocuChargeCredit[1:]
        cTBDocuChargeCreditFloat = float(cTBDocuChargeCreditComma.replace(",", ""))
        ## print("cTBDocuChargeCreditFloat::", cTBDocuChargeCreditFloat)

        # # SGST(9%)
        cTBSGSTComma = cTB_SGSTCredit[1:]
        cTBSGSTFloat = round(float(cTBSGSTComma.replace(",", "")))
        ## print("cTBSGSTFloat::", cTBSGSTFloat)

        # # CGST(9%)
        cTBCGSTComma = cTB_CGSTCredit[1:]
        cTBCGSTFloat = float(cTBCGSTComma.replace(",", ""))
        ## print("cTBCGSTFloat::", cTBCGSTFloat)
        #
        #  # INSURANCE CHARGES
        cTB_InsuChargCreditComma = cTB_InsuChargCredit[1:]
        cTB_InsuChargCreditFloat = float(cTB_InsuChargCreditComma.replace(",", ""))
        ## print("cTB_InsuChargCreditFloat::", cTB_InsuChargCreditFloat)

        # TOTAL CHARGES TO BORROWER by adding all charges
        totalChargOfChToBorrElem = cTBProssFeesCreditFloat + cTBStampDutyCreditFloat + cTBOnlConvFeesCreditFloat + cTBDocuChargeCreditFloat + cTBSGSTFloat + cTBCGSTFloat + cTB_InsuChargCreditFloat
        print("totalChargOfChToBorrElem::", totalChargOfChToBorrElem)
        ## print("cTBTotalCredit::", cTBTotalCredit)

        cTBTotalCreditComma = cTBTotalCredit[1:]
        cTBTotalCreditFloat = float(cTBTotalCreditComma.replace(",", ""))
        print("cTBTotalCreditFloat::", cTBTotalCreditFloat)

        try:
            try:
                if round(cTBTotalCreditFloat) == round(totalChargOfChToBorrElem):
                    print("cTBTotalCreditFloat matched with totalChargOfChToBorrElem")
                else:
                    print("Exception::cTBTotalCreditFloat not matched with totalChargOfChToBorrElem")

                assert round(cTBTotalCreditFloat) == round(totalChargOfChToBorrElem)

            except:
                if round(cTBTotalCreditFloat) == round(totalChargOfChToBorrElem + 0.5):
                    print("cTBTotalCreditFloat matched with totalChargOfChToBorrElem")
                else:
                    print("Exception::cTBTotalCreditFloat not matched with totalChargOfChToBorrElem")

                assert round(cTBTotalCreditFloat) == round(totalChargOfChToBorrElem + 0.5)

        except:
            if round(cTBTotalCreditFloat) == round(totalChargOfChToBorrElem - 0.38):
                print("cTBTotalCreditFloat matched with totalChargOfChToBorrElem")
            else:
                print("Error::cTBTotalCreditFloat not matched with totalChargOfChToBorrElem")

            assert round(cTBTotalCreditFloat) == round(totalChargOfChToBorrElem - 0.38)

            print("********************************************************************************")

    def test_getDisbSummaryDisAmtToBor(self, url):
        global disbAmtTOBorrFloat

        # DISBURSED AMOUNT TO BORROWER
        disbAmtTOBorrComma = disbAmtTOBorr[1:]
        disbAmtTOBorrFloat = float(disbAmtTOBorrComma.replace(",", ""))
        print("disbAmtTOBorrFloat::", disbAmtTOBorrFloat)
        print("lATB_totalDebitFloat::", lATB_totalDebitFloat)
        print("cTBTotalCreditFloat::", cTBTotalCreditFloat)

        totalDisbAmtTOBorrFloat = lATB_totalDebitFloat - cTBTotalCreditFloat
        print("totalDisbAmtTOBorrFloat::", totalDisbAmtTOBorrFloat)

        try:
            try:

                if lATB_totalDebitFloat - cTBTotalCreditFloat == disbAmtTOBorrFloat:
                    print(
                        "Substraction of lATB_totalDebitFloat and cTBTotalCreditTotalFloat matched with disbAmtTOBorrFloat")
                else:
                    print(
                        "Exception::Substraction of lATB_totalDebitFloat and cTBTotalCreditTotalFloat not matched with disbAmtTOBorrFloat")

                assert lATB_totalDebitFloat - cTBTotalCreditFloat == disbAmtTOBorrFloat

            except:
                if (round(lATB_totalDebitFloat) - round(cTBTotalCreditFloat)) == round(disbAmtTOBorrFloat):
                    print(
                        "Substraction of lATB_totalDebitFloat and cTBTotalCreditTotalFloat matched with disbAmtTOBorrFloat")
                else:
                    print(
                        "Exception::Substraction of lATB_totalDebitFloat and cTBTotalCreditTotalFloat not matched with disbAmtTOBorrFloat")

                assert (round(lATB_totalDebitFloat) - round(cTBTotalCreditFloat)) == round(disbAmtTOBorrFloat)

        except:
            try:
                if (round(lATB_totalDebitFloat) - round(cTBTotalCreditFloat)) == round(disbAmtTOBorrFloat - 1):
                    print(
                        "Substraction of lATB_totalDebitFloat and cTBTotalCreditTotalFloat matched with disbAmtTOBorrFloat")
                else:
                    print(
                        "Exception::Substraction of lATB_totalDebitFloat and cTBTotalCreditTotalFloat not matched with disbAmtTOBorrFloat")

                assert (round(lATB_totalDebitFloat) - round(cTBTotalCreditFloat)) == round(disbAmtTOBorrFloat - 1)

            except:
                if (round(lATB_totalDebitFloat) - round(cTBTotalCreditFloat)) == round(disbAmtTOBorrFloat + 0.5):
                    print(
                        "Substraction of lATB_totalDebitFloat and cTBTotalCreditTotalFloat matched with disbAmtTOBorrFloat")
                else:
                    print(
                        "Error::Substraction of lATB_totalDebitFloat and cTBTotalCreditTotalFloat not matched with disbAmtTOBorrFloat")

                assert (round(lATB_totalDebitFloat) - round(cTBTotalCreditFloat)) == round(disbAmtTOBorrFloat + 0.5)

            print("********************************************************************************")


    def test_getDisbSummaryTotalAmtCred(self, url):

        # TOTAL AMOUNT
        totalAmountCreditComma = totalAmountCredit[1:]
        totalAmountCreditFloat = float(totalAmountCreditComma.replace(",", ""))
        print("totalAmountCreditFloat::", totalAmountCreditFloat)
        print("cTBTotalCreditFloat::", cTBTotalCreditFloat)
        print("disbAmtTOBorrFloat::", disbAmtTOBorrFloat)

        try:

            if cTBTotalCreditFloat + disbAmtTOBorrFloat == totalAmountCreditFloat:
                print("Addition of cTBTotalCreditFloat and disbAmtTOBorrFloat matched with totalAmountCreditFloat")
            else:
                print(
                    "Exception::Addition of cTBTotalCreditFloat and disbAmtTOBorrFloat not matched with totalAmountCreditFloat")

            assert cTBTotalCreditFloat + disbAmtTOBorrFloat == totalAmountCreditFloat

        except:

            if (round(cTBTotalCreditFloat) + round(disbAmtTOBorrFloat)) == round(totalAmountCreditFloat):
                print("Addition of cTBTotalCreditFloat and disbAmtTOBorrFloat matched with totalAmountCreditFloat")
            else:
                print(
                    "Error::Addition of cTBTotalCreditFloat and disbAmtTOBorrFloat not matched with totalAmountCreditFloat")

            assert (round(cTBTotalCreditFloat) + round(disbAmtTOBorrFloat)) == round(totalAmountCreditFloat)

        print("********************************************************************************")

    def test_getDisbSummaryTotalAmtDebit(self, url):

        # '''getting transaction/allDisbursedLoans'''

        # print('status code of get DisbursedLoans::', response5.status_code)
        # print(response5.json())

        allDisbursedLoans = response5.json()["data"]["rows"]
        #
        # print(allDisbursedLoans)
        #
        approvedAmt = []
        #
        for ea in allDisbursedLoans:
            if "Approved amount" in ea:
                approvedAmt.append(ea["Approved amount"])
        #
        ## print(approvedAmt)

        approvedAmtTotal = round(sum(approvedAmt), 2)
        print("approvedAmtTotal::", approvedAmtTotal)
        #
        print("lATB_totalDebitInt::", lATB_totalDebitInt)

        if approvedAmtTotal == lATB_totalDebitInt:
            print("approvedAmtTotal matched with lATB_totalDebitInt")
        else:
            print("Error::approvedAmtTotal not matched with lATB_totalDebitInt")

        assert approvedAmtTotal == lATB_totalDebitInt

        print("********************************************************************************")

    def test_getRepaySummary(self, url):

        '''getting tally/getAllRepaymentData'''
        # print('status code of get tally/getAllRepaymentData::', response2.status_code)
        # print(response2.json())

        # TOTAL REPAID AMOUNT FROM BORROWER
        total_loans = response2.json()["data"]["totalLoan"]
        print("total_loans in repayment::", total_loans)

        tRepaidAmountFromBorrowerCreditTotal = response2.json()["data"]["titles"][0]["credit"]

        # '''getting transaction/allRepaidLoans'''

        # print('status code of get Upcoming EMI::', response4.status_code)
        # print(response4.json())

        allTransRepay = response4.json()["data"]["rows"]

        # print(allTransRepay)

        repaidAmt = []

        for rd in allTransRepay:
            if "Repaid amount" in rd:
                repaidAmt.append(rd["Repaid amount"])

        # print(repaidAmt)

        totalRepayTransAmt = round(sum(repaidAmt), 2)
        print("totalRepayTransAmt::", totalRepayTransAmt)

        # print("tRepaidAmountFromBorrowerCreditTotal::",tRepaidAmountFromBorrowerCreditTotal)

        tRepaidAmountFromBorrowerCreditTotalComma = tRepaidAmountFromBorrowerCreditTotal[1:]
        tRepaidAmountFromBorrowerCreditTotalFloat = round(
            float(tRepaidAmountFromBorrowerCreditTotalComma.replace(",", "")), 2)
        print("tRepaidAmountFromBorrowerCreditTotalFloat::", tRepaidAmountFromBorrowerCreditTotalFloat)

        if totalRepayTransAmt == tRepaidAmountFromBorrowerCreditTotalFloat:
            print("totalRepayTransAmt matched with tRepaidAmountFromBorrowerCreditTotalFloat")
        else:
            print("Error::totalRepayTransAmt not matched with tRepaidAmountFromBorrowerCreditTotalFloat")

        assert totalRepayTransAmt == tRepaidAmountFromBorrowerCreditTotalFloat

        print("********************************************************************************")
