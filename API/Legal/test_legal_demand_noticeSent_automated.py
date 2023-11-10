import requests
import pytest
from datetime import datetime, timedelta

currentFullTime = datetime.now()  # whole date
currentDateStr = datetime.strftime(currentFullTime,"%Y-%m-%d") # date to string format
currentDateF = datetime.strptime(currentDateStr,"%Y-%m-%d") # string to date format

previousDate = currentDateF - timedelta(days=1)
previousDateStr = datetime.strftime(previousDate,"%Y-%m-%d")

previousDate_2 = currentDateF - timedelta(days=2)
previousDateStr_2 = datetime.strftime(previousDate_2,"%Y-%m-%d")

previousDate_6 = currentDateF - timedelta(days=6)
previousDateStr_6 = datetime.strftime(previousDate_6,"%Y-%m-%d")


# print("currentDateFormat::",currentDateF)
print("currentDateStr::",currentDateStr)
# print("previousDate::",previousDate)
print("previousDateStr::",previousDateStr)
print("previousDateStr_2::",previousDateStr_2)
print("previousDateStr_6::",previousDateStr_6)

# note: execute at 12 pm every time because of crone set time.

class TestLegal:
    @pytest.fixture
    def url(self):
        global legalDemandLetter, legalAutoDebit, legalNotice, legalNotice2, legalNotice3
        legalDemandLetter = requests.get("https://lendittfinserve.com/prod/admin/legal/getAllLegalData",
                                         params={"page": 1, "startDate": f"{previousDateStr_6}T10:00:00.000Z",
                                                 "endDate": f"{previousDateStr_6}T10:00:00.000Z", "type": 1, "adminId": 134,
                                                 "download": "true"})  # date = 6 days before notice sent

        legalNotice = requests.get("https://lendittfinserve.com/prod/admin/legal/getAllLegalData",
                                   params={"page": 1, "startDate": f"{currentDateStr}T10:00:00.000Z",
                                           "endDate": f"{currentDateStr}T10:00:00.000Z", "type": 2, "adminId": 134,
                                           "download": "true"})  # current date

        legalNotice2 = requests.get("https://lendittfinserve.com/prod/admin/legal/getAllLegalData",
                                    params={"page": 1, "startDate": f"{previousDateStr}T10:00:00.000Z",
                                            "endDate": f"{previousDateStr}T10:00:00.000Z", "type": 2, "adminId": 134,
                                            "download": "true"})  # 1 day previous to notice sent

        legalNotice3 = requests.get("https://lendittfinserve.com/prod/admin/legal/getAllLegalData",
                                    params={"page": 1, "startDate": f"{previousDateStr_2}T10:00:00.000Z",
                                            "endDate": f"{previousDateStr_2}T10:00:00.000Z", "type": 2, "adminId": 134,
                                            "download": "true"})  # previous to notice sent 2


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

        print("count of demand loan ids::", len(loanID))
        # print("unpaid loan ids::",loanID)
        # print(demandCreatedDate)
        # print(emiNo)
        # print(asOnDueAmt)
        # print(dueDate)

        uLIdSet = set(loanID)
        uniqLIdList = list(uLIdSet)
        print("count of demand unique loan ids list ::", len(uniqLIdList))
        print("demand loan ids::", loanID)
        print("demand uniqLIdList::", uniqLIdList)

    def test_NoticeSent(self, url):
        global lIdNS, missedDemandWithNotice, matchedDemandWithNotice
        countOfNoticeSent = legalNotice.json()["data"]["count"]
        print("countOfNoticeSent::", countOfNoticeSent)

        noticeAllData = legalNotice.json()["data"]["rows"]
        # print(noticeAllData)

        lIdNS = []
        legalCrDateNS = []
        typeNS = []
        adPlDateNS = []
        daysPostLetterSentNS = []

        for ns in noticeAllData:
            if ns["Loan ID"]:
                lIdNS.append(ns["Loan ID"])

            if ns["Legal created date"]:
                legalCrDateNS.append(ns["Legal created date"])

            if ns["Type"]:
                typeNS.append(ns["Type"])

            if ns["AD placed date"]:
                adPlDateNS.append(ns["AD placed date"])

            if ns["Days post letter sent"]:
                daysPostLetterSentNS.append(ns["Days post letter sent"])

        print("lIdNS::", lIdNS)
        # print(legalCrDateNS)
        # print(typeNS)
        # print(adPlDateNS)
        # print(daysPostLetterSentNS)

        matchedDemandWithNotice = []
        missedDemandWithNotice = []

        # checking demand against notice sent
        for unl in uniqLIdList:
            if unl in lIdNS:
                matchedDemandWithNotice.append(unl)
                # print("loanID in lIdNS::", unl)

            if unl not in lIdNS:
                missedDemandWithNotice.append(unl)
                # print("loanID not in lIdNS::", unl)


    def test_NoticeSent2(self, url):
        global missedNoticeSent2

        noticeAllData2 = legalNotice2.json()["data"]["rows"]
        # print(noticeAllData)

        lIdNS2 = []

        for ns in noticeAllData2:
            if ns["Loan ID"]:
                lIdNS2.append(ns["Loan ID"])

        print("lIdNS2::", lIdNS2)

        missedNoticeSent2 = []
        for mDN in missedDemandWithNotice:
            if mDN not in lIdNS2:
                missedNoticeSent2.append(mDN)

        print("missedNoticeSent2::",missedNoticeSent2)


    def test_NoticeSent3(self, url):

        noticeAllData3 = legalNotice3.json()["data"]["rows"]
        # print(noticeAllData)

        lIdNS3 = []

        for ns in noticeAllData3:
            if ns["Loan ID"]:
                lIdNS3.append(ns["Loan ID"])

        print("lIdNS3::", lIdNS3)

        missedNoticeSent3 = []
        for mDN in missedNoticeSent2:
            if mDN not in lIdNS3:
                missedNoticeSent3.append(mDN)

        print("missedNoticeSent3::",missedNoticeSent3)


        countOfMissedDemandWithNotice3 = len(missedNoticeSent3)
        print("count of missedNoticeSent3::", countOfMissedDemandWithNotice3)

        if countOfMissedDemandWithNotice3 == 0:
            print("demand letter matched with notice menu in legal section")
        else:
            print("demand letter not matched with notice menu in legal section")
        assert countOfMissedDemandWithNotice3 == 0
