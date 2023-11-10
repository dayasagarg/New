import requests
import pytest
from datetime import datetime, timedelta

start = datetime.strptime("2023-10-25", "%Y-%m-%d") # 7 day ago from end
end = datetime.strptime("2023-11-01", "%Y-%m-%d") # 7 days ago date from current date(end_2)


start_2 = datetime.strptime("2023-10-24", "%Y-%m-%d") # 15 days ago from end date 2
end_2 = datetime.strptime("2023-11-08", "%Y-%m-%d")  # current date
# date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

start_date = start.strftime("%Y-%m-%d")
end_date = end.strftime("%Y-%m-%d")

start_date_2 = start_2.strftime("%Y-%m-%d")
end_date_2 = end_2.strftime("%Y-%m-%d")


print("start_date::", start_date)
print("end_date::", end_date)

print("start_date_2::", start_date_2)
print("end_date_2::", end_date_2)



# note: execute at 12 pm every time because of crone set time.

class TestLegal:
    @pytest.fixture
    def url(self):
        global legalDemandLetter, legalAutoDebit, legalNotice, todayAutoDebitFailed,todayAutoDebitFailed2
        legalDemandLetter = requests.get("https://lendittfinserve.com/prod/admin/legal/getAllLegalData",
                                         params={"page": 1, "startDate": f"{start_date_2}T10:00:00.000Z",
                                                 "endDate": f"{end_date_2}T10:00:00.000Z", "type": 1, "adminId": 134,
                                                 "download": "true"})  # date = 5 days before todayAutoDebitFailed

        todayAutoDebitFailed = requests.get("https://lendittfinserve.com/prod/admin/dashboard/todayAutoDebitData",
                                            params={"pagesize": 10, "start_date": f"{start_date}T10:00:00.000Z",
                                                    "end_date": f"{end_date}T10:00:00.000Z", "status": 4,
                                                    "page": 1})  # current day after demand letter



    def test_DemandLetter(self, url):
        global loanID, uniqLIdList
        countOfLegalDemandLetter = legalDemandLetter.json()["data"]["count"]
        print("countOfLegalDemandLetter::", countOfLegalDemandLetter)

        demandAllData = legalDemandLetter.json()["data"]["rows"]
        # print(demandAllData)

        loanID = []
        demandCreatedDate = []
        custName = []
        loanTenure = []
        disburseDate = []
        loanAmt = []
        emiNo = []
        asOnDueAmt = []
        dueDate = []
        totalPenaltyDays = []
        emi1Date = []
        emi1Amt = []
        emi1Penalty = []
        emi1Status = []

        emi2Date = []
        emi2Amt = []
        emi2Penalty = []
        emi2Status = []

        emi3Date = []
        emi3Amt = []
        emi3Penalty = []
        emi3Status = []

        receivedPartPayment = []
        adPlAmt = []
        adPlDate = []
        adSource = []
        amtPaidBeforeLetter = []
        amtPaidAfterLetter = []

        emailDate = []
        daysPostLetterSent = []

        for ld in demandAllData:
            if ld["Emi 3 status"] == "UNPAID":
                if ld["Loan ID"]:
                    loanID.append(ld["Loan ID"])

                if ld["Demand created date"]:
                    demandCreatedDate.append(ld["Demand created date"])

                if ld["EMI number"]:
                    emiNo.append(ld["EMI number"])

                if ld["As on due amount"]:
                    asOnDueAmt.append(ld["As on due amount"])

                if ld["Due date"]:
                    dueDate.append(ld["Due date"])

                if ld["Emi 1 date"]:
                    emi1Date.append(ld["Emi 1 date"])

                if ld["Emi 1 status"]:
                    emi1Status.append(ld["Emi 1 status"])

                if ld["Emi 2 date"]:
                    emi2Date.append(ld["Emi 2 date"])

                if ld["Emi 2 status"]:
                    emi2Status.append(ld["Emi 2 status"])

                if ld["Emi 3 date"]:
                    emi3Date.append(ld["Emi 3 date"])

                if ld["Emi 3 status"]:
                    emi3Status.append(ld["Emi 3 status"])

                if ld["AD placed date"]:
                    adPlDate.append(ld["AD placed date"])

                if ld["Email date"]:
                    emailDate.append(ld["Email date"])

            if ld["Emi 2 status"] == "UNPAID" and (ld["Emi 3 status"] == "UNPAID" or ld["Emi 3 status"] == "-"):
                if ld["Loan ID"]:
                    loanID.append(ld["Loan ID"])

                if ld["Demand created date"]:
                    demandCreatedDate.append(ld["Demand created date"])

                if ld["EMI number"]:
                    emiNo.append(ld["EMI number"])

                if ld["As on due amount"]:
                    asOnDueAmt.append(ld["As on due amount"])

                if ld["Due date"]:
                    dueDate.append(ld["Due date"])

                if ld["Emi 1 date"]:
                    emi1Date.append(ld["Emi 1 date"])

                if ld["Emi 1 status"]:
                    emi1Status.append(ld["Emi 1 status"])

                if ld["Emi 2 date"]:
                    emi2Date.append(ld["Emi 2 date"])

                if ld["Emi 2 status"]:
                    emi2Status.append(ld["Emi 2 status"])

                if ld["Emi 3 date"]:
                    emi3Date.append(ld["Emi 3 date"])

                if ld["Emi 3 status"]:
                    emi3Status.append(ld["Emi 3 status"])

                if ld["AD placed date"]:
                    adPlDate.append(ld["AD placed date"])

                if ld["Email date"]:
                    emailDate.append(ld["Email date"])

            if (ld["Emi 1 status"] == "UNPAID" and (ld["Emi 2 status"] == "UNPAID" or ld["Emi 2 status"] == "-") and (
                    ld["Emi 3 status"] == "UNPAID" or ld["Emi 3 status"] == "-")):
                if ld["Loan ID"]:
                    loanID.append(ld["Loan ID"])

                if ld["Demand created date"]:
                    demandCreatedDate.append(ld["Demand created date"])

                if ld["EMI number"]:
                    emiNo.append(ld["EMI number"])

                if ld["As on due amount"]:
                    asOnDueAmt.append(ld["As on due amount"])

                if ld["Due date"]:
                    dueDate.append(ld["Due date"])

                if ld["Emi 1 date"]:
                    emi1Date.append(ld["Emi 1 date"])

                if ld["Emi 1 status"]:
                    emi1Status.append(ld["Emi 1 status"])

                if ld["Emi 2 date"]:
                    emi2Date.append(ld["Emi 2 date"])

                if ld["Emi 2 status"]:
                    emi2Status.append(ld["Emi 2 status"])

                if ld["Emi 3 date"]:
                    emi3Date.append(ld["Emi 3 date"])

                if ld["Emi 3 status"]:
                    emi3Status.append(ld["Emi 3 status"])

                if ld["AD placed date"]:
                    adPlDate.append(ld["AD placed date"])

                if ld["Email date"]:
                    emailDate.append(ld["Email date"])

        print("count of unpaid loan ids::", len(loanID))
        # print("unpaid loan ids::",loanID)
        # print(demandCreatedDate)
        # print(emiNo)
        # print(asOnDueAmt)
        # print(dueDate)

        uLIdSet = set(loanID)
        uniqLIdList = list(uLIdSet)
        print("count of unpaid unique loan ids list ::", len(uniqLIdList))
        print("unpaid uniqLIdList::", uniqLIdList)

    def test_AutoDebit(self, url):
        global missedDemandWithAutoDebit

        countOfAutoDebit = todayAutoDebitFailed.json()["data"]["count"]
        print("countOfAutoDebit::", countOfAutoDebit)

        autoDebitAllData = todayAutoDebitFailed.json()["data"]["finalData"]
        # print(autoDebitAllData)
        #
        loanID_AD = []

        for ad in autoDebitAllData:
            if ad["AD Placed by"] == "System" and ad["EMI type"] == "FULLPAY":
                loanID_AD.append(ad["Loan ID"])

        #
        print("loanID_AD::", loanID_AD)

        matchedDemandWithAutoDebit = []
        missedDemandWithAutoDebit = []
        #
        # # checking demand against AutoDebit
        for uln in uniqLIdList:
            if uln in loanID_AD:
                matchedDemandWithAutoDebit.append(uln)
                # print("loanID in loanIDAD::", uln)
            #
            if uln not in loanID_AD:
                missedDemandWithAutoDebit.append(uln)
                # print("loanID not in loanIDAD::", uln)
        #
        print("matchedDemandWithAutoDebit::", matchedDemandWithAutoDebit)
        print("missedDemandWithAutoDebit::", missedDemandWithAutoDebit)
        countOfMissedDemandWithAutoDebit = len(missedDemandWithAutoDebit)
        print("count of missedDemandWithAutoDebit::", countOfMissedDemandWithAutoDebit)




        if countOfMissedDemandWithAutoDebit == 0:
            print("Defaulter Demand letter matched with legal AutoDebit menu")
        else:
            print("Defaulter Demand letter not matched with legal AutoDebit menu")

        assert countOfMissedDemandWithAutoDebit == 0


