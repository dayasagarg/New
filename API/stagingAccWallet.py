import pytest
import requests
from requests.auth import HTTPBasicAuth
import json
import time
from datetime import datetime


class TestAccountWallet:
    @pytest.fixture
    def url(self):
        global walletSettlAPIResp, razPay1, razPay2, cashFree

        '''# WALLET SETTLEMENT TOTAL'''
        walletSettlAPIResp = requests.get(
            "https://lendittfinserve.com/prod/admin/tally/getWalletSettlementDetails?startDate=2023-10-06T10%3A00%3A00.000Z&endDate=2023-10-06T10%3A00%3A00.000Z")  # current date

        '''# RAZORPAY-1'''
        razPay1 = requests.get("https://api.razorpay.com/v1/settlements",
                               params={"from":1696464000,"to":1696550400},
                                auth=HTTPBasicAuth("rzp_live_b6RhLeN8cATRGq", "mLimxgzWR1vuOaamr5IvU8MC"),
                                ) #from date = previous date, #to date = current date (in unix format)

        '''# RAZORPAY-2'''
        razPay2 = requests.get("https://api.razorpay.com/v1/settlements",
                               params={"from": 1696464000, "to": 1696550400},
                               auth=HTTPBasicAuth("rzp_live_QBApq2NUwCxSDx", "tXl5Bj5ovyc07NSaBaTs0j1J")
                               )  # #from date = previous date, #to date = current date (in unix format)

        '''# CASH FREE'''
        data = {"pagination": {"limit": 100},
                "filters": {"start_date": "2023-10-05T18:30:00+05:30",
                            "end_date": "2023-10-06T18:30:00+05:30"}}  # start date = previous date, end date = current date

        cashFree = requests.post("https://api.cashfree.com/pg/settlements",
                                 headers={"x-client-id": "162761aa6de3f33933ad43d749167261",
                                          "x-client-secret": "5c14eb7b1e0e7ffdcf413ba242f669ea8becc5a6",
                                          "x-api-version": "2022-09-01"},
                                 auth=HTTPBasicAuth("162761aa6de3f33933ad43d749167261",
                                                    "5c14eb7b1e0e7ffdcf413ba242f669ea8becc5a6"), json=data
                                 )


    def test_getTallyAccountWalletRazor1(self,url):
        '''tally/getWalletSettlementDetails'''

        global walletRaz1GSTDebitFloat, walletRaz1ChargDebitFloat, amtReceivedInRaz1DebitFloat, walletRaz2GSTDebitFloat, walletRaz2ChargDebitFloat, amtReceivedInRaz2DebitFloat, amtReceivedInCashFreeDebitTotalFloat
        global TotalOfWalletSettlementDebitFloat
        global TotalOfWalletSettlementCreditFloat
        global walletRaz1CreditTotalFloat
        global walletRaz1CreditTotalFloat
        global TotalOfWalletSettlementDebitFloat



        '''# WALLET SETTLEMENT TOTAL'''

        # print('status code of get Upcoming EMI::', walletSettlAPIResp.status_code)
        # print(walletSettlAPIResp.json())


        # RAZORPAY-1
        walletRaz1 = walletSettlAPIResp.json()["data"]["titles"][0]
        walletRaz1NameTotal = walletSettlAPIResp.json()["data"]["titles"][0]["name"]
        walletRaz1DebitTotal = walletSettlAPIResp.json()["data"]["titles"][0]["debit"]
        walletRaz1CreditTotal = walletSettlAPIResp.json()["data"]["titles"][0]["credit"]

        print("walletRaz1CreditTotal::", walletRaz1CreditTotal)
        walletRaz1CreditTotalComma = walletRaz1CreditTotal[1:]
        walletRaz1CreditTotalFloat = float(walletRaz1CreditTotalComma.replace(",", ""))
        print("walletRaz1CreditTotalFloat::", walletRaz1CreditTotalFloat)

        # RAZORPAY SETTLEMENT
        walletRaz1Settl = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"]
        walletRaz1SettlName = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][0]["name"]
        walletRaz1SettlDebit = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][0]["debit"]
        walletRaz1SettlCredit = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][0]["credit"]

        print("walletRaz1SettlCredit::", walletRaz1SettlCredit)
        walletRaz1SettlCreditComma = walletRaz1SettlCredit[1:]
        walletRaz1SettlCreditFloat = float(walletRaz1SettlCreditComma.replace(",", ""))
        print("walletRaz1SettlCreditFloat::", walletRaz1SettlCreditFloat)

        # RAZORPAY GST
        walletRaz1GST = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"]
        walletRaz1GSTName = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][1]["name"]
        walletRaz1GSTDebit = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][1]["debit"]
        walletRaz1GSTCredit = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][1]["credit"]

        print("walletRaz1GSTDebit::", walletRaz1GSTDebit)
        walletRaz1GSTDebitComma = walletRaz1GSTDebit[1:]
        walletRaz1GSTDebitFloat = float(walletRaz1GSTDebitComma.replace(",", ""))
        print("walletRaz1GSTDebitFloat::", walletRaz1GSTDebitFloat)

        # RAZORPAY CHARGES
        walletRaz1Charg = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"]
        walletRaz1ChargName = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][2]["name"]
        walletRaz1ChargDebit = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][2]["debit"]
        walletRaz1ChargCredit = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][2]["credit"]

        print("walletRaz1ChargDebit::", walletRaz1ChargDebit)
        walletRaz1ChargDebitComma = walletRaz1ChargDebit[1:]
        walletRaz1ChargDebitFloat = float(walletRaz1ChargDebitComma.replace(",", ""))
        print("walletRaz1ChargDebitFloat::", walletRaz1ChargDebitFloat)


        # # RAZORPAY REFUND
        # Raz1RefundName = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][3]["name"]
        # Raz1RefundDebit = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][3]["debit"]
        # Raz1RefundCredit = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][3]["credit"]
        #
        # print("Raz1RefundDebit::", Raz1RefundDebit)
        # Raz1RefundDebitComma = Raz1RefundDebit[1:]
        # Raz1RefundDebitFloat = float(Raz1RefundDebitComma.replace(",", ""))
        # print("Raz1RefundDebitFloat::", Raz1RefundDebitFloat)


        # AMOUNT RECIEVED IN
        amtReceivedInRaz1Name = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][3]["name"]
        amtReceivedInRaz1Debit = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][3]["debit"]
        amtReceivedInRaz1Credit = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][3]["credit"]

        print("amtReceivedInRaz1Debit::", amtReceivedInRaz1Debit)
        amtReceivedInRaz1DebitComma = amtReceivedInRaz1Debit[1:]
        amtReceivedInRaz1DebitFloat = float(amtReceivedInRaz1DebitComma.replace(",", ""))
        print("amtReceivedInRaz1DebitFloat::", amtReceivedInRaz1DebitFloat)

        # ICICI BANK - 30400
        amtReceivedInRaz1ICICI30400Name = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][3]["section"][0]["name"]
        amtReceivedInRaz1ICICI30400Debit = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][3]["section"][0]["debit"]
        amtReceivedInRaz1ICICI30400Credit = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][3]["section"][0]["credit"]

        # print("amtReceivedInRaz1ICICI30400Debit::", amtReceivedInRaz1ICICI30400Debit)
        # amtReceivedInRaz1ICICI30400DebitComma = amtReceivedInRaz1ICICI30400Debit[1:]
        # amtReceivedInRaz1ICICI30400DebitFloat = float(amtReceivedInRaz1ICICI30400DebitComma.replace(",", ""))
        # print("amtReceivedInRaz1ICICI30400DebitFloat::", amtReceivedInRaz1ICICI30400DebitFloat)

        # ICICI BANK - 753
        amtReceivedInRaz1ICICI753Name = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][3]["section"][1][
            "name"]
        amtReceivedInRaz1ICICI753Debit = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][3]["section"][1][
            "debit"]
        amtReceivedInRaz1ICICI753Credit = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][3]["section"][1][
            "credit"]

        print("amtReceivedInRaz1ICICI753Debit::", amtReceivedInRaz1ICICI753Debit)
        amtReceivedInRaz1ICICI753DebitComma = amtReceivedInRaz1ICICI753Debit[1:]
        amtReceivedInRaz1ICICI753DebitFloat = float(amtReceivedInRaz1ICICI753DebitComma.replace(",", ""))
        print("amtReceivedInRaz1ICICI753DebitFloat::", amtReceivedInRaz1ICICI753DebitFloat)

        # RBL BANK
        amtReceivedInRaz1RBLBankName = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][3]["section"][2]["name"]
        amtReceivedInRaz1RBLBankDebit = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][3]["section"][2]["debit"]
        amtReceivedInRaz1RBLBankCredit = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][3]["section"][2]["credit"]

        # print("amtReceivedInRaz1RBLBankDebit::", amtReceivedInRaz1RBLBankDebit)
        # amtReceivedInRaz1RBLBankDebitComma = amtReceivedInRaz1RBLBankDebit[1:]
        # amtReceivedInRaz1RBLBankDebitFloat = float(amtReceivedInRaz1RBLBankDebitComma.replace(",", ""))
        # print("amtReceivedInRaz1RBLBankDebitFloat::", amtReceivedInRaz1RBLBankDebitFloat)


        #Total of wallet settlement
        TotalOfWalletSettlementName = walletSettlAPIResp.json()["data"]["titles"][3]["name"]
        TotalOfWalletSettlementDebit = walletSettlAPIResp.json()["data"]["titles"][3]["debit"]
        TotalOfWalletSettlementCredit = walletSettlAPIResp.json()["data"]["titles"][3]["credit"]

        print("TotalOfWalletSettlementDebit::", TotalOfWalletSettlementDebit)
        TotalOfWalletSettlementDebitComma = TotalOfWalletSettlementDebit[1:]
        TotalOfWalletSettlementDebitFloat = float(TotalOfWalletSettlementDebitComma.replace(",", ""))
        print("TotalOfWalletSettlementDebitFloat::", TotalOfWalletSettlementDebitFloat)

        print("TotalOfWalletSettlementCredit::", TotalOfWalletSettlementCredit)
        TotalOfWalletSettlementCreditComma = TotalOfWalletSettlementCredit[1:]
        TotalOfWalletSettlementCreditFloat = float(TotalOfWalletSettlementCreditComma.replace(",", ""))
        print("TotalOfWalletSettlementCreditFloat::", TotalOfWalletSettlementCreditFloat)
        print("************************************************************************************")


    def test_getRazor1Settl(self,url):

        global raz1Amount

        # print(razPay1.json())

        ## sData = razPay1.json()
        ## jData = json.dumps(sData)
        # print(jData)

        raz1All = razPay1.json()["items"]
        now = datetime.now()
        today_time = now.strftime("%m/%d/%Y")
        print("today_time::", today_time)

        for ra in raz1All:
            createdAt = ra["created_at"]
            dt = datetime.fromtimestamp(createdAt)
            settlement_time = dt.strftime("%m/%d/%Y")

            print(today_time, settlement_time)

            if today_time == settlement_time:
                raz1Amount = ra["amount"]
                print("raz1Amount::", raz1Amount)# in paisa

                print("walletRaz1CreditTotalFloat::", walletRaz1CreditTotalFloat)  # in rupees

                if walletRaz1CreditTotalFloat == (raz1Amount/100):
                    print("walletRaz1CreditTotalFloat is matched with raz1Amount")
                else:
                    print("walletRaz1CreditTotalFloat is not matched with raz1Amount")

                assert walletRaz1CreditTotalFloat == (raz1Amount/100)  # in rupees

    print("************************************************************************************")



    def test_getTallyAccountWalletRazor2(self,url):
        #RAZORPAY-2

        global walletRaz2CreditTotalFloat,walletRaz2GSTDebitFloat,walletRaz2ChargDebitFloat,amtReceivedInRaz2DebitFloat, raz2Amount, Raz2RefundDebitFloat

        walletRaz2Name = walletSettlAPIResp.json()["data"]["titles"][1]["name"]
        walletRaz2DebitTotal = walletSettlAPIResp.json()["data"]["titles"][1]["debit"]
        walletRaz2CreditTotal = walletSettlAPIResp.json()["data"]["titles"][1]["credit"]

        print("walletRaz2CreditTotal::", walletRaz2CreditTotal)
        walletRaz2CreditTotalComma = walletRaz2CreditTotal[1:]
        walletRaz2CreditTotalFloat = float(walletRaz2CreditTotalComma.replace(",", ""))
        print("walletRaz2CreditTotalFloat::", walletRaz2CreditTotalFloat)


        #RAZORPAY SETTLEMENT
        walletRaz2Settl = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"]
        walletRaz2SettlName = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"][0]["name"]
        walletRaz2SettlDebit = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"][0]["debit"]
        walletRaz2SettlCredit = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"][0]["credit"]

        print("walletRaz2SettlCredit::", walletRaz2SettlCredit)
        walletRaz2SettlCreditComma = walletRaz2SettlCredit[1:]
        walletRaz2SettlCreditFloat = float(walletRaz2SettlCreditComma.replace(",", ""))
        print("walletRaz2SettlCreditFloat::", walletRaz2SettlCreditFloat)


        # #RAZORPAY GST
        walletRaz2GST = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"]
        walletRaz2GSTName = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"][1]["name"]
        walletRaz2GSTDebit = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"][1]["debit"]
        walletRaz2GSTCredit = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"][1]["credit"]
        #
        print("walletRaz2GSTDebit::", walletRaz2GSTDebit)
        walletRaz2GSTDebitComma = walletRaz2GSTDebit[1:]
        walletRaz2GSTDebitFloat = float(walletRaz2GSTDebitComma.replace(",", ""))
        print("walletRaz2GSTDebitFloat::", walletRaz2GSTDebitFloat)

        # #RAZORPAY CHARGES
        walletRaz2Charg = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"]
        walletRaz2ChargName = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"][2]["name"]
        walletRaz2ChargDebit = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"][2]["debit"]
        walletRaz2ChargCredit = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"][2]["credit"]
        #

        print("walletRaz2ChargDebit::", walletRaz2ChargDebit)
        walletRaz2ChargDebitComma = walletRaz2ChargDebit[1:]
        walletRaz2ChargDebitFloat = float(walletRaz2ChargDebitComma.replace(",", ""))
        print("walletRaz2ChargDebitFloat::", walletRaz2ChargDebitFloat)

        # # RAZORPAY REFUND
        # Raz2RefundName = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][3]["name"]
        # Raz2RefundDebit = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][3]["debit"]
        # Raz2RefundCredit = walletSettlAPIResp.json()["data"]["titles"][0]["subtitles"][3]["credit"]
        #
        # print("Raz2RefundDebit::", Raz2RefundDebit)
        # Raz2RefundDebitComma = Raz2RefundDebit[1:]
        # Raz2RefundDebitFloat = float(Raz2RefundDebitComma.replace(",", ""))
        # print("Raz2RefundDebitFloat::", Raz2RefundDebitFloat)


        # #AMOUNT RECIEVED IN Raz2
        amtReceivedInRaz2Name = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"][3]["name"]
        amtReceivedInRaz2Debit = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"][3]["debit"]
        amtReceivedInRaz2Credit = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"][3]["credit"]
        #

        print("amtReceivedInRaz2Debit::", amtReceivedInRaz2Debit)
        amtReceivedInRaz2DebitComma = amtReceivedInRaz2Debit[1:]
        amtReceivedInRaz2DebitFloat = float(amtReceivedInRaz2DebitComma.replace(",", ""))
        print("amtReceivedInRaz2DebitFloat::", amtReceivedInRaz2DebitFloat)


        # #ICICI BANK - 30400
        amtReceivedInRaz2ICICI30400Name = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"][3]["section"][0]["name"]
        amtReceivedInRaz2ICICI30400Debit = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"][3]["section"][0]["debit"]
        amtReceivedInRaz2ICICI30400Credit = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"][3]["section"][0]["credit"]
        #

        # print("amtReceivedInRaz2ICICI30400Debit::", amtReceivedInRaz2ICICI30400Debit)
        # amtReceivedInRaz2ICICI30400DebitComma = amtReceivedInRaz2ICICI30400Debit[1:]
        # amtReceivedInRaz2ICICI30400DebitFloat = float(amtReceivedInRaz2ICICI30400DebitComma.replace(",", ""))
        # print("amtReceivedInRaz2ICICI30400DebitFloat::", amtReceivedInRaz2ICICI30400DebitFloat)
        #

        # #ICICI BANK - 753
        amtReceivedInRaz2ICICI753Name = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"][3]["section"][1]["name"]
        amtReceivedInRaz2ICICI753Debit = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"][3]["section"][1]["debit"]
        amtReceivedInRaz2ICICI753Credit = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"][3]["section"][1]["credit"]

        print("amtReceivedInRaz2ICICI753Debit::", amtReceivedInRaz2ICICI753Debit)
        amtReceivedInRaz2ICICI753DebitComma = amtReceivedInRaz2ICICI753Debit[1:]
        amtReceivedInRaz2ICICI753DebitFloat = float(amtReceivedInRaz2ICICI753DebitComma.replace(",", ""))
        print("amtReceivedInRaz2ICICI753DebitFloat::", amtReceivedInRaz2ICICI753DebitFloat)


        # #RBL BANK
        amtReceivedInRaz2RBLBankName = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"][3]["section"][2]["name"]
        amtReceivedInRaz2RBLBankDebit = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"][3]["section"][2]["debit"]
        amtReceivedInRaz2RBLBankCredit = walletSettlAPIResp.json()["data"]["titles"][1]["subtitles"][3]["section"][2]["credit"]

        # print("amtReceivedInRaz2RBLBankDebit::", amtReceivedInRaz2RBLBankDebit)
        # amtReceivedInRaz2RBLBankDebitComma = amtReceivedInRaz2RBLBankDebit[1:]
        # amtReceivedInRaz2RBLBankDebitFloat = float(amtReceivedInRaz2RBLBankDebitComma.replace(",", ""))
        # print("amtReceivedInRaz2RBLBankDebitFloat::", amtReceivedInRaz2RBLBankDebitFloat)



        # print(razPay2.json())

        # sData = razPay2.json()
        # jData = json.dumps(sData)
        # print(jData)

        raz2All = razPay2.json()["items"]
        now = datetime.now()
        today_time = now.strftime("%m/%d/%Y")
        print("today_time::", today_time)
        #

        for ra2 in raz2All:
            createdAt = ra2["created_at"]
            dt = datetime.fromtimestamp(createdAt)
            settlement_time = dt.strftime("%m/%d/%Y")

            print(today_time, settlement_time)

            if today_time == settlement_time:
                raz2Amount = ra2["amount"]
                print("raz2Amount::", raz2Amount) # in paisa
        #
                print("walletRaz2CreditTotalFloat::", walletRaz2CreditTotalFloat)  # in rupees

                if walletRaz2CreditTotalFloat == (raz2Amount/100):
                    print("walletRaz2CreditTotalFloat is matched with raz2Amount")
                else:
                    print("walletRaz2CreditTotalFloat is not matched with raz2Amount")

                assert walletRaz2CreditTotalFloat == (raz2Amount/100)  # in rupees

    print("************************************************************************************")


    def test_getTallyAccountWalletCashfree(self,url):
        global walletCashFreeGSTDebitFloat, walletCashFreeChargDebitFloat, walletCashFreeRefundDebitFloat, walletCashFreeCreditTotalFloat,amtReceivedInCashFreeDebitTotalFloat

        #CASHFREE
        walletCashFree = walletSettlAPIResp.json()["data"]["titles"][2]
        walletCashFreeName = walletSettlAPIResp.json()["data"]["titles"][2]["name"]
        walletCashFreeDebitTotal = walletSettlAPIResp.json()["data"]["titles"][2]["debit"]
        walletCashFreeCreditTotal = walletSettlAPIResp.json()["data"]["titles"][2]["credit"]

        print("walletCashFreeCreditTotal::",walletCashFreeCreditTotal)
        walletCashFreeCreditTotalComma = walletCashFreeCreditTotal[1:]
        walletCashFreeCreditTotalFloat = float(walletCashFreeCreditTotalComma.replace(",", ""))
        print("walletCashFreeCreditTotalFloat::", walletCashFreeCreditTotalFloat)

        #CASHFREE SETTLEMENT
        walletCashFreeSettl = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"]
        walletCashFreeSettlName = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][0]["name"]
        walletCashFreeSettlDebit = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][0]["debit"]
        walletCashFreeSettlCredit = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][0]["credit"]

        # print("walletCashFreeSettlDebit::",walletCashFreeSettlDebit)
        # walletCashFreeSettlDebitComma = walletCashFreeSettlDebit[1:]
        # walletCashFreeSettlDebitFloat = float(walletCashFreeSettlDebitComma.replace(",", ""))
        # print("walletCashFreeSettlDebitFloat::", walletCashFreeSettlDebitFloat)

        print("walletCashFreeSettlCredit::",walletCashFreeSettlCredit)
        walletCashFreeSettlCreditComma = walletCashFreeSettlCredit[1:]
        walletCashFreeSettlCreditFloat = float(walletCashFreeSettlCreditComma.replace(",", ""))
        print("walletCashFreeSettlCreditFloat::", walletCashFreeSettlCreditFloat)

        # #CASHFREE  GST
        walletCashFreeGST = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"]
        walletCashFreeGSTName = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][1]["name"]
        walletCashFreeGSTDebit = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][1]["debit"]
        walletCashFreeGSTCredit = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][1]["credit"]

        print("walletCashFreeGSTDebit::",walletCashFreeGSTDebit)
        walletCashFreeGSTDebitComma = walletCashFreeGSTDebit[1:]
        walletCashFreeGSTDebitFloat = float(walletCashFreeGSTDebitComma.replace(",", ""))
        print("walletCashFreeGSTDebitFloat::", walletCashFreeGSTDebitFloat)


        # # #CASHFREE  CHARGES
        walletCashFreeCharg = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"]
        walletCashFreeChargName = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][2]["name"]
        walletCashFreeChargDebit = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][2]["debit"]
        walletCashFreeChargCredit = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][2]["credit"]

        print("walletCashFreeChargDebit::",walletCashFreeChargDebit)
        walletCashFreeChargDebitComma = walletCashFreeChargDebit[1:]
        walletCashFreeChargDebitFloat = float(walletCashFreeChargDebitComma.replace(",", ""))
        print("walletCashFreeChargDebitFloat::", walletCashFreeChargDebitFloat)

        # #CASHFREE REFUND
        walletCashFreeRefundName = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][3]["name"]
        walletCashFreeRefundDebit = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][3]["debit"]
        walletCashFreeRefundCredit = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][3]["credit"]

        print("walletCashFreeRefundDebit::", walletCashFreeRefundDebit)
        walletCashFreeRefundDebitComma = walletCashFreeRefundDebit[1:]
        walletCashFreeRefundDebitFloat = float(walletCashFreeRefundDebitComma.replace(",", ""))
        print("walletCashFreeRefundDebitFloat::", walletCashFreeRefundDebitFloat)

        # # #AMOUNT RECIEVED IN CASHFREE
        amtReceivedInCashFreeName = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][4]["name"]
        amtReceivedInCashFreeDebitTotal = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][4]["debit"]
        amtReceivedInCashFreeCreditTotal = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][4]["credit"]
        #
        print("amtReceivedInCashFreeDebitTotal::", amtReceivedInCashFreeDebitTotal)
        amtReceivedInCashFreeDebitTotalComma = amtReceivedInCashFreeDebitTotal[1:]
        amtReceivedInCashFreeDebitTotalFloat = float(amtReceivedInCashFreeDebitTotalComma.replace(",", ""))
        print("amtReceivedInCashFreeDebitTotalFloat::", amtReceivedInCashFreeDebitTotalFloat)

        # # #ICICI BANK - 30400
        amtReceivedInICICI30400CashFreeName = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][4]["section"][0]["name"]
        amtReceivedInICICI30400CashFreeDebit = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][4]["section"][0]["debit"]
        amtReceivedInICICI30400CashFreeCredit = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][4]["section"][0]["credit"]
        # #
        # print("amtReceivedInICICI30400CashFreeDebit::", amtReceivedInICICI30400CashFreeDebit)
        # amtReceivedInICICI30400CashFreeDebitComma = amtReceivedInICICI30400CashFreeDebit[1:]
        # amtReceivedInICICI30400CashFreeDebitFloat = float(amtReceivedInICICI30400CashFreeDebitComma.replace(",", ""))
        # print("amtReceivedInICICI30400CashFreeDebitFloat::", amtReceivedInICICI30400CashFreeDebitFloat)

        # # #ICICI BANK - 753
        amtReceivedInICICI753CashFreeName = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][4]["section"][1]["name"]
        amtReceivedInICICI753CashFreeDebit = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][4]["section"][1]["debit"]
        amtReceivedInICICI753CashFreeCredit = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][4]["section"][1]["credit"]
        #
        print("amtReceivedInICICI753CashFreeDebit::", amtReceivedInICICI753CashFreeDebit)
        amtReceivedInICICI753CashFreeDebitComma = amtReceivedInICICI753CashFreeDebit[1:]
        amtReceivedInICICI753CashFreeDebitFloat = float(amtReceivedInICICI753CashFreeDebitComma.replace(",", ""))
        print("amtReceivedInICICI753CashFreeDebitFloat::", amtReceivedInICICI753CashFreeDebitFloat)

        # # #RBL BANK
        amtReceivedInRBLBankCashFreeName = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][4]["section"][2]["name"]
        amtReceivedInRBLBankCashFreeDebit = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][4]["section"][2]["debit"]
        amtReceivedInRBLBankCashFreeCredit = walletSettlAPIResp.json()["data"]["titles"][2]["subtitles"][4]["section"][2]["credit"]

        # print("amtReceivedInRBLBankCashFreeDebit::", amtReceivedInRBLBankCashFreeDebit)
        # amtReceivedInRBLBankCashFreeDebitComma = amtReceivedInRBLBankCashFreeDebit[1:]
        # amtReceivedInRBLBankCashFreeDebitFloat = float(amtReceivedInRBLBankCashFreeDebitComma.replace(",", ""))
        # print("amtReceivedInRBLBankCashFreeDebitFloat::", amtReceivedInRBLBankCashFreeDebitFloat)


        #EXPENSES ON ACCOUNT OF REFERRAL
        ExpensesOnAccountReferDebit = walletSettlAPIResp.json()["data"]["expenseReferral"]["debit"]
        ExpensesOnAccountReferCredit = walletSettlAPIResp.json()["data"]["expenseReferral"]["credit"]

    print("************************************************************************************")


    def test_postCashfreeSettl(self,url):

        global totalOfSerSettlTax, totalOfSerSettlCharg, totalOfAdj, totalOfAmtSettl

        # print(cashFree.json())
        # print(cashFree.status_code)

        # string_data = cashFree.json()
        # json_data = json.dumps(string_data)
        # print(json_data)

        serTaxList = []
        settlTaxList = []
        serChargList = []
        settlChargList = []
        adjustList = []
        amtSettlList = []

        cashFreeAllData = cashFree.json()["data"]
        # print(cashFreeAllData)

        for cf in cashFreeAllData:
            try:
                if cf["service_tax"]:
                    serTaxList.append(cf["service_tax"])
                    print("serTaxList::", serTaxList)


            except KeyError:
                pass
                print("service_tax not avail in next element")

            try:
                if cf["settlement_tax"]:
                    settlTaxList.append(cf["settlement_tax"])
                    print("settlTaxList::", settlTaxList)


            except KeyError:
                pass
                print("settlement_tax not avail in next element")

                # print("settlTaxList::", settlTaxList)


            try:
                if cf["service_charge"]:
                    serChargList.append(cf["service_charge"])


            except KeyError:
                pass
                print("service_charge not avail in next element")
                print("serChargList::", serChargList)


            try:
                if cf["settlement_charge"]:
                    settlChargList.append(cf["settlement_charge"])


            except KeyError:
                pass
                print("settlement_charge not avail in next element")
                print("settlChargList::", settlChargList)

            try:
                if cf["adjustment"]:
                    adjustList.append(-cf["adjustment"])  # keep adj amt positive


            except KeyError:
                pass
                print("adjustList not avail in next element")
                print("adjustList::", adjustList)

            try:
                if cf["amount_settled"]:
                    amtSettlList.append(cf["amount_settled"])


            except KeyError:
                pass
                print("amtSettlList not avail in next element")
                print("amtSettlList::", amtSettlList)

            totalOfSerSettlTax = sum(serTaxList) + sum(settlTaxList)
            print("totalOfSerSettlTax::", totalOfSerSettlTax)

            totalOfSerSettlCharg = round(sum(serChargList) + sum(settlChargList), 2)
            print("totalOfSerSettlCharg::", totalOfSerSettlCharg)

            totalOfAdj = round(sum(adjustList), 2)
            print("totalOfAdj::", totalOfAdj)

            totalOfAmtSettl = round(sum(amtSettlList), 2)
            print("totalOfAmtSettl::", totalOfAmtSettl)

        if walletCashFreeGSTDebitFloat == round(totalOfSerSettlTax,2):
            print("walletCashFreeGSTDebitFloat matched with totalOfSerSettlTax")
        else:
            print("walletCashFreeGSTDebitFloat not matched with totalOfSerSettlTax")

        assert walletCashFreeGSTDebitFloat == round(totalOfSerSettlTax,2)

        if walletCashFreeChargDebitFloat == totalOfSerSettlCharg:
            print("walletCashFreeChargDebitFloat matched with totalOfSerSettlCharg")
        else:
            print("walletCashFreeChargDebitFloat not matched with totalOfSerSettlCharg")

        assert walletCashFreeChargDebitFloat == totalOfSerSettlCharg

        if walletCashFreeRefundDebitFloat == totalOfAdj:
            print("walletCashFreeRefundDebitFloat matched with totalOfAdj")
        else:
            print("walletCashFreeRefundDebitFloat not matched with totalOfAdj")

        assert walletCashFreeRefundDebitFloat == totalOfAdj

        if amtReceivedInCashFreeDebitTotalFloat == totalOfAmtSettl:
            print("amtReceivedInCashFreeDebitTotalFloat matched with totalOfAmtSettl")
        else:
            print("amtReceivedInCashFreeDebitTotalFloat not matched with totalOfAmtSettl")

        assert amtReceivedInCashFreeDebitTotalFloat == totalOfAmtSettl

    print("************************************************************************************")


    def test_getTallyAccountWalletTotal(self,url):

        grandTotalOfWalletDebit = round((walletRaz1GSTDebitFloat + walletRaz1ChargDebitFloat + amtReceivedInRaz1DebitFloat  + walletRaz2GSTDebitFloat + walletRaz2ChargDebitFloat + amtReceivedInRaz2DebitFloat  + walletCashFreeGSTDebitFloat + walletCashFreeChargDebitFloat + amtReceivedInCashFreeDebitTotalFloat - walletCashFreeRefundDebitFloat ),2)
        print("grandTotalOfWallet::", grandTotalOfWalletDebit)

        # grandTotalOfWalletDebit = round((walletRaz1GSTDebitFloat + walletRaz1ChargDebitFloat + amtReceivedInRaz1DebitFloat - Raz2RefundDebitFloat + walletRaz2GSTDebitFloat + walletRaz2ChargDebitFloat + amtReceivedInRaz2DebitFloat - Raz2RefundDebitFloat + walletCashFreeGSTDebitFloat + walletCashFreeChargDebitFloat + amtReceivedInCashFreeDebitTotalFloat - walletCashFreeRefundDebitFloat ),2)
        # print("grandTotalOfWallet::", grandTotalOfWalletDebit)

        if TotalOfWalletSettlementDebitFloat == grandTotalOfWalletDebit:
            print("TotalOfWalletSettlementDebitFloat matched with grandTotalOfWalletDebit")

        else:
            print("TotalOfWalletSettlementDebitFloat not matched with grandTotalOfWalletDebit")

        assert TotalOfWalletSettlementDebitFloat == grandTotalOfWalletDebit


        grandTotalOfWalletCredit = round((walletRaz1CreditTotalFloat + walletRaz2CreditTotalFloat + walletCashFreeCreditTotalFloat), 2)
        print("grandTotalOfWalletCredit::", grandTotalOfWalletCredit)

        if TotalOfWalletSettlementCreditFloat == grandTotalOfWalletCredit:
            print("TotalOfWalletSettlementCreditFloat matched with grandTotalOfWalletCredit")

        else:
            print("TotalOfWalletSettlementCreditFloat not matched with grandTotalOfWalletCredit")

        assert TotalOfWalletSettlementCreditFloat == grandTotalOfWalletCredit

        print("************************************************************************************")


