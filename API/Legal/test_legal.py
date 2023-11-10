import requests
import pytest
# note: execute at 12 pm every time because of crone set time.

class TestLegal:
    @pytest.fixture
    def url(self):
        global legalDemandLetter, legalAutoDebit, legalNotice, todayAutoDebitFailed
        legalDemandLetter = requests.get("https://lendittfinserve.com/prod/admin/legal/getAllLegalData",
                                         params={"page": 1, "startDate": "2023-10-14T10:00:00.000Z",
                                                 "endDate": "2023-10-14T10:00:00.000Z", "type": 1, "adminId": 134,
                                                 "download": "true"}) # date = 5/6 days before notice sent

        legalAutoDebit = requests.get("https://lendittfinserve.com/prod/admin/legal/autoDebitList",
                                      params={"page": 1, "startDate": "2023-10-15T10:00:00.000Z",
                                              "endDate": "2023-10-15T10:00:00.000Z",
                                              "download": "true"})  # 4 days after demand letter

        #### todayAutoDebitFailed = requests.get("https://lendittfinserve.com/prod/admin/dashboard/todayAutoDebitData",params={"pagesize":10,"start_date":"2023-10-11T10:00:00.000Z","end_date":"2023-10-11T10:00:00.000Z","status":4,"page":1})

        legalNotice = requests.get("https://lendittfinserve.com/prod/admin/legal/getAllLegalData",
                                   params={"page": 1, "startDate": "2023-10-20T10:00:00.000Z",
                                           "endDate": "2023-10-20T10:00:00.000Z", "type": 2, "adminId": 134,
                                           "download": "true"})  # 1 days after auto debit / 5 days after demand letter / current date


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
        countOfAutoDebit = legalAutoDebit.json()["data"]["count"]
        print("countOfAutoDebit::",countOfAutoDebit)

        autoDebitAllData = legalAutoDebit.json()["data"]["rows"]
        # print(autoDebitAllData)

        loanIDAD = []
        placDateAD = []
        autoDebit = []
        statusAD = []

        for ad in autoDebitAllData:
            if ad["Loan id"]:
                loanIDAD.append(ad["Loan id"])

            if ad["Place date"]:
                placDateAD.append(ad["Place date"])

            if ad["Auto-debit"]:
                autoDebit.append(ad["Auto-debit"])

            if ad["Status"]:
                statusAD.append(ad["Status"])

        print(loanIDAD)
        # print(placDateAD)
        # print(autoDebit)
        # print(statusAD)

        matchedDemandWithAutoDebit = []
        missedDemandWithAutoDebit = []

        # checking demand against AutoDebit
        for uln in uniqLIdList:
            if uln in loanIDAD:
                matchedDemandWithAutoDebit.append(uln)
                # print("loanID in loanIDAD::", uln)

            if uln not in loanIDAD:
                missedDemandWithAutoDebit.append(uln)
                # print("loanID not in loanIDAD::", uln)

        print("matchedDemandWithAutoDebit::", matchedDemandWithAutoDebit)
        print("missedDemandWithAutoDebit::", missedDemandWithAutoDebit)
        countOfMissedDemandWithAutoDebit = len(missedDemandWithAutoDebit)
        print("count of missedDemandWithAutoDebit::", countOfMissedDemandWithAutoDebit)






        ### allDataDefaulterAutoDebit = todayAutoDebitFailed.json()["data"]["finalData"]
        # print("allDataDefaulterAutoDebit::",allDataDefaulterAutoDebit)
        #
        #
        # ### defaultAutoDebitLId = []
        # for dad in allDataDefaulterAutoDebit:
        #     if dad["Loan ID"]:
        #         defaultAutoDebitLId.append(dad["Loan ID"])
        #
        #
        # print("defaultAutoDebitLId::",defaultAutoDebitLId)








    #
    # def test_NoticeSent(self, url):
    #     countOfNoticeSent = legalNotice.json()["data"]["count"]
    #     print("countOfNoticeSent::", countOfNoticeSent)
    #
    #     noticeAllData = legalNotice.json()["data"]["rows"]
    #     # print(noticeAllData)
    #
    #     lIdNS = []
    #     legalCrDateNS = []
    #     typeNS = []
    #     adPlDateNS = []
    #     daysPostLetterSentNS = []
    #
    #     for ns in noticeAllData:
    #         if ns["Loan ID"]:
    #             lIdNS.append(ns["Loan ID"])
    #
    #         if ns["Legal created date"]:
    #             legalCrDateNS.append(ns["Legal created date"])
    #
    #         if ns["Type"]:
    #             typeNS.append(ns["Type"])
    #
    #         if ns["AD placed date"]:
    #             adPlDateNS.append(ns["AD placed date"])
    #
    #         if ns["Days post letter sent"]:
    #             daysPostLetterSentNS.append(ns["Days post letter sent"])
    #
    #
    #     print("lIdNS::",lIdNS)
    #     # print(legalCrDateNS)
    #     # print(typeNS)
    #     # print(adPlDateNS)
    #     # print(daysPostLetterSentNS)
    #
    #     matchedDemandWithNotice = []
    #     missedDemandWithNotice = []
    #
    #     # checking demand against notice sent
    #     for unl in uniqLIdList:
    #         if unl in lIdNS:
    #             matchedDemandWithNotice.append(unl)
    #             # print("loanID in lIdNS::", unl)
    #
    #         if unl not in lIdNS:
    #             missedDemandWithNotice.append(unl)
    #             # print("loanID not in lIdNS::", unl)
    #
    #
    #     print("matchedDemandWithNotice::", matchedDemandWithNotice)
    #     countOfMatchedDemandWithNotice = len(matchedDemandWithNotice)
    #     print("count of matchedDemandWithNotice::", countOfMatchedDemandWithNotice)
    #
    #     print("missedDemandWithNotice::", missedDemandWithNotice)
    #     countOfMissedDemandWithNotice = len(missedDemandWithNotice)
    #     print("count of missedDemandWithNotice::", countOfMissedDemandWithNotice)
    #
    #     if countOfMissedDemandWithNotice == 0:
    #         print("demand letter matched with notice menu in legal section")
    #     else:
    #         print("demand letter not matched with notice menu in legal section")
    #     assert countOfMissedDemandWithNotice == 0
    #




