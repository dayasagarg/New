from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time
import pypdf
from datetime import datetime
from datetime import timedelta
import json
import math


# JSON reader
file = open("input.json")
info = json.load(file)
email = info["user1"]["email"]
password = info["user1"]["password"]
otp = info["user1"]["otp"]
loanID = info["user1"]["loanID"]
loanPdf = info["user1"]["loanPdf"]


# PDF reader
reader = pypdf.PdfReader(loanPdf)  # pdf file location
firstPage = reader.pages[0].extract_text()
thirdPage = reader.pages[2].extract_text()
fourthPage = reader.pages[3].extract_text()
sixthPage = reader.pages[5].extract_text()
seventhPage = reader.pages[6].extract_text()
eighthPage = reader.pages[7].extract_text()
ninthPage = reader.pages[8].extract_text()
eleventhPage = reader.pages[10].extract_text()


class TestDashRepo:
    @pytest.fixture()
    def setup_teardown(self):
        global driver

        ser = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service = ser)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://lendittfinserve.com/lenditt/#/dashboard") # url
        time.sleep(1)
        driver.find_element(By.ID, "email").send_keys(email) #email
        # time.sleep(1)
        driver.find_element(By.ID, "login-btn").click() #button
        # time.sleep(1)
        driver.find_element(By.ID, "login-password").send_keys(password) #password
        # time.sleep(1)
        driver.find_element(By.ID, "login-btn2").click() #button
        # time.sleep(1)
        driver.find_element(By.ID, "OTP").send_keys(otp) #otp
        # time.sleep(1)
        element = driver.find_element(By.ID, "login-btn2") #button
        # time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        # time.sleep(1)
        driver.find_element(By.ID,"login-btn2").click() #button
        time.sleep(1)
        yield
        time.sleep(1)
        driver.close()
        driver.quit()
        print("test execution completed")


    def test_keyFactStatement(self, setup_teardown):
        driver.find_element(By.ID, "mainSearch").send_keys(loanID)  # search box
        time.sleep(2)
        driver.find_element(By.ID, "master-search-name-mobile").click()  #click user
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(1)


        '''SCHEDULE-CUM-KEY FACT STATEMENT'''

        # Name of Borrower
        profileName = driver.find_element(By.ID,"user-full-name").text
        time.sleep(2)
        print(f"### 'profileName':'{profileName}' ###")
        time.sleep(1)

        try:
            if profileName in firstPage:
                print(f" *** 'profileName':'{profileName}' is matched with KEY FACT STATEMENT in first Page of pdf *** ")
            else:
                print(f"Exception :: 'profileName':'{profileName}' is not matched with KEY FACT STATEMENT in first Page of pdf ")

            assert profileName in firstPage, "profileName is matched with KEY FACT STATEMENT in first Page of pdf"

        except:
            if 'Name of Borrower' in firstPage:
                index1 = firstPage.index('Name of Borrower')
                index2 = firstPage.index('NBFC NameChinmay Finlease')
                text = firstPage[index1 + 16:index2]
                print(f"Name by pdf module :: {text}")



        # #loanId
        loanId = driver.find_element(By.XPATH,"//div//table[@id='loanDetails']//tbody[1]//tr[1]//td//a").text
        time.sleep(2)
        if loanId in firstPage:
            print(f" *** 'loanId' :'{loanId}' is matched with KEY FACT STATEMENT in first Page of pdf *** ")
        else:
            print(f"Error :: 'loanId' :'{loanId}' is not matched with KEY FACT STATEMENT in first Page of pdf ")

        assert loanId in firstPage, "loanId is matched with KEY FACT STATEMENT in first Page of pdf"


        # Date of Signing
        try:
            loanAppDate = driver.find_element(By.XPATH, "(//div//table[@id='loanDetails']//tbody[1]//tr[1]//td)[6]").text
            time.sleep(1)
            LoanApplicationDate = loanAppDate.replace('/','-')

            if LoanApplicationDate in firstPage:
                print(f" *** 'LoanApplicationDate' :'{LoanApplicationDate}' is matched with KEY FACT STATEMENT in first Page of pdf *** ")
            else:
                print(
                    f" *** 'LoanApplicationDate' :'{LoanApplicationDate}' is not matched with KEY FACT STATEMENT in first Page of pdf *** ")


            assert LoanApplicationDate in firstPage, "LoanApplicationDate is matched with KEY FACT STATEMENT in first Page of pdf"

        except:
            try:
                loanAppDate = driver.find_element(By.XPATH,"(//div//table[@id='loanDetails']//tbody[1]//tr[1]//td)[5]").text
                time.sleep(1)
                LoanApplicationDate = loanAppDate.replace('/', '-')

                if LoanApplicationDate in firstPage:
                    print(f" *** 'LoanApplicationDate' :'{LoanApplicationDate}' is matched with KEY FACT STATEMENT in first Page of pdf *** ")
                else:
                    print(f"Exception :: 'LoanApplicationDate' :'{LoanApplicationDate}' is not matched with KEY FACT STATEMENT in first Page of pdf ")

                assert LoanApplicationDate in firstPage, "LoanApplicationDate is matched with KEY FACT STATEMENT in first Page of pdf"

            except:

                if 'Date of Signing' in firstPage:
                    index1 = firstPage.index('Date of Signing')
                    index2 = firstPage.index('Name of Borrower')
                    text = firstPage[index1 + 28:index2]
                    print(f"Name by pdf :: {text}")


                # print("LoanApplicationDateA",LoanApplicationDate)


        '''LOAN DETAILS'''
        # # Loan Amount
        apprAmount = driver.find_element(By.XPATH,"(//div//table[@id='loanDetails']//tbody[1]//tr[1]//td)[9]").text
        time.sleep(2)
        lSpace = apprAmount.replace(" ","")
        approvedAmount = lSpace + '.00/-'
        approvedAmount2 = lSpace + '/-'
        try:
            if approvedAmount in firstPage:
                print(f" *** 'approvedAmount' :'{approvedAmount}' is matched with LOAN DETAILS in first Page of pdf *** ")
            else:
                print(f"Exception :: 'approvedAmount' :'{approvedAmount}' is not matched with LOAN DETAILS in first Page of pdf ")

            assert approvedAmount in firstPage, "approvedAmount is matched with LOAN DETAILS in first Page of pdf"
        except:
            if approvedAmount2 in firstPage:
                print(
                    f" *** 'approvedAmount2' :'{approvedAmount2}' is matched with LOAN DETAILS in first Page of pdf *** ")
            else:
                print(
                    f"Error :: 'approvedAmount2' :'{approvedAmount2}' is not matched with LOAN DETAILS in first Page of pdf ")

            assert approvedAmount2 in firstPage, "approvedAmount2 is matched with LOAN DETAILS in first Page of pdf"


        # Interest Rate (per Day)
        loanIntPerDay = driver.find_element(By.XPATH,"(//div//table[@id='loanDetails']//tbody[1]//tr[1]//td)[8]").text
        time.sleep(1)
        loanInterestPerDay = loanIntPerDay.replace(" %","00%")
        loanInterestPerDay2 = loanIntPerDay.replace(" %", "%")
        loanInterestPerDay3 = loanIntPerDay.replace(" %", "0%")
        try:
            if loanInterestPerDay in firstPage:
                print(f" *** 'loanInterestPerDay' :'{loanInterestPerDay}' is matched with LOAN DETAILS in first Page of pdf *** ")
            else:
                print(f"Exception :: 'loanInterestPerDay' :'{loanInterestPerDay}' is not matched with LOAN DETAILS in first Page of pdf ")

            assert loanInterestPerDay in firstPage, "loanInterestPerDay is matched with LOAN DETAILS in first Page of pdf"

        except:

            try:
                if loanInterestPerDay2 in firstPage:
                    print(
                        f" *** 'loanInterestPerDay2' :'{loanInterestPerDay2}' is matched with LOAN DETAILS in first Page of pdf *** ")
                else:
                    print(
                        f"Exception :: 'loanInterestPerDay2' :'{loanInterestPerDay2}' is not matched with LOAN DETAILS in first Page of pdf ")

                assert loanInterestPerDay2 in firstPage, "loanInterestPerDay is matched with LOAN DETAILS in first Page of pdf"

            except:

                if loanInterestPerDay3 in firstPage:
                    print(
                        f" *** 'loanInterestPerDay3' :'{loanInterestPerDay3}' is matched with LOAN DETAILS in first Page of pdf *** ")
                else:
                    print(
                        f"Error :: 'loanInterestPerDay3' :'{loanInterestPerDay3}' is not matched with LOAN DETAILS in first Page of pdf ")

                assert loanInterestPerDay3 in firstPage, "loanInterestPerDay3 is matched with LOAN DETAILS in first Page of pdf"


        # # Interest Rate (per Annum)
        strLIPD = loanIntPerDay.replace(" %","")
        flotLIPD = float(strLIPD)
        loanIntPerAnnum = flotLIPD * 365
        loanIntPerAnnumFl = round(float(loanIntPerAnnum),2)
        loanIntPerAnnumStr = str(loanIntPerAnnumFl)
        # print("loanIntPerAnnumStr::",loanIntPerAnnumStr)

        loanIntPerAnnumInt = int(loanIntPerAnnum)
        loanIntPerAnnumStr2 = str(loanIntPerAnnumInt)
        # print("loanIntPerAnnumStr2::", loanIntPerAnnumStr2)

        try:
            if loanIntPerAnnumStr in firstPage:
                print(f" *** 'loanIntPerAnnumStr' :'{loanIntPerAnnumStr}%' is matched with LOAN DETAILS in first Page of pdf *** ")
            else:
                print(f"Exception :: 'loanIntPerAnnumStr' :'{loanIntPerAnnumStr}%'  is not matched with LOAN DETAILS in first Page of pdf ")

            assert loanIntPerAnnumStr in firstPage, "loanIntPerAnnumStr is matched with LOAN DETAILS in first Page of pdf"
        except:
            if loanIntPerAnnumStr2 in firstPage:
                print(f" *** 'loanIntPerAnnumStr2' :'{loanIntPerAnnumStr2}%' is matched with LOAN DETAILS in first Page of pdf *** ")
            else:
                print(f"Error :: 'loanIntPerAnnumStr2' :'{loanIntPerAnnumStr2}%'  is not matched with LOAN DETAILS in first Page of pdf ")

            assert loanIntPerAnnumStr2 in firstPage, "loanIntPerAnnumStr2 is matched with LOAN DETAILS in first Page of pdf"


        # # Insurance premium amount
        inPremAmount = driver.find_element(By.XPATH,"(//div//table[@id='loanDetails']//tbody[1]//tr[1]//td)[10]").text
        time.sleep(1)
        insurancePremAmount = inPremAmount.replace(" ","")
        if insurancePremAmount in firstPage:
            print(f" *** 'insurancePremAmount' :'{insurancePremAmount}' is matched with LOAN DETAILS in first Page of pdf *** ")
        else:
            print(f"Error :: 'insurancePremAmount' :'{insurancePremAmount}' is not matched with LOAN DETAILS in first Page of pdf ")

        assert insurancePremAmount in firstPage, "insurancePremAmount is matched with LOAN DETAILS in first Page of pdf"


        # # # Loan Tenure
        loanDurInDays = driver.find_element(By.XPATH,"(//div//table[@id='loanDetails']//tbody[1]//tr[1]//td)[16]").text
        time.sleep(1)
        loanDurationInDays = loanDurInDays + " Days"
        if loanDurationInDays in firstPage:
            print(f" *** 'loanDurationInDays' :'{loanDurationInDays}' is matched with LOAN DETAILS in first Page of pdf *** ")
        else:
            print(f"Error :: 'loanDurationInDays' :'{loanDurationInDays}' is not matched with LOAN DETAILS in first Page of pdf ")

        assert loanDurationInDays in firstPage, "loanDurationInDays is matched with LOAN DETAILS in first Page of pdf"


        # # Loan Start Date
        loanDisbDate = driver.find_element(By.XPATH,"(//div//table[@id='loanDetails']//tbody[1]//tr[1]//td)[6]").text
        time.sleep(1)
        loanDisbursedDate = loanDisbDate.replace("/","-")

        try:
            if loanDisbursedDate in firstPage:
                print(f" *** 'loanDisbursedDate' :'{loanDisbursedDate}' is matched with LOAN DETAILS in first Page of pdf *** ")
            else:
                print(f"Exception :: 'loanDisbursedDate' :'{loanDisbursedDate}' is not matched with LOAN DETAILS in first Page of pdf ")

            assert loanDisbursedDate in firstPage, "loanDisbursedDate is matched with LOAN DETAILS in first Page of pdf"

        except:

            if 'Loan Start Date' in firstPage:
                indexLSD = firstPage.index('Loan Start Date')
                indexIA = firstPage.index('Interest Amount')
                text = firstPage[indexLSD + 16:indexIA]
                print(f"By pdf :: {text}")


        # Loan End Date
        loanStartDate = datetime.strptime(loanDisbursedDate,"%d-%m-%Y")
        loanEndDateTimeFromY = loanStartDate + timedelta(days=int(loanDurInDays)-1)
        loanEndDateFromD = datetime.strftime(loanEndDateTimeFromY,'%d-%m-%Y')
        loanEndDate = str(loanEndDateFromD).split(" ")[0]

        loanEndDateTimeFromY2 = loanStartDate + timedelta(days=int(loanDurInDays) - 2)
        loanEndDateFromD2 = datetime.strftime(loanEndDateTimeFromY2, '%d-%m-%Y')
        loanEndDate2 = str(loanEndDateFromD2).split(" ")[0]

        try:
            if loanEndDate in firstPage:
                print(f" *** 'loanEndDate' :'{loanEndDate}' is matched with LOAN DETAILS in first Page of pdf *** ")

            assert loanEndDate in firstPage, "loanEndDate is matched with LOAN DETAILS in first Page of pdf"

        except:
            if loanEndDate2 in firstPage:
                print(f" *** 'loanEndDate2' :'{loanEndDate2}' is matched with LOAN DETAILS in first Page of pdf *** ")
            else:
                print(f"Error :: 'loanEndDate2' :'{loanEndDate2}' is not matched with LOAN DETAILS in first Page of pdf ")

            assert loanEndDate2 in firstPage, "loanEndDate2 is matched with LOAN DETAILS in first Page of pdf"


        '''CHARGES (All charges are non-refundable & applicable post disbursement of loan)'''
        rmLoanAmInt = apprAmount.replace("₹ ","")
        rmChLoanAmInt = rmLoanAmInt.replace(",","")
        loanAmountInt = int(rmChLoanAmInt)

        # #Processing Charges @6.5%
        processChargeInt = math.ceil((loanAmountInt/100) * 6.5)
        processChargeInt2 = int((loanAmountInt / 100) * 6.5)

        processChargeString = format(processChargeInt)
        processChargeRs = "₹" + processChargeString
        processCharge = processChargeRs[0] + processChargeRs[1] +","+ processChargeRs[2:]

        processChargeString2 = format(processChargeInt2)
        processChargeRs2 = "₹" + processChargeString2
        processCharge2 = processChargeRs2[0] + processChargeRs2[1] + "," + processChargeRs2[2:]


        #
        try:
            if processCharge in firstPage:
                print(f" *** 'processCharge' :'{processCharge}' is matched with CHARGES Section in first Page of pdf *** ")
            else:
                print(f"Exception :: 'processCharge' :'{processCharge}' is not matched with CHARGES Section in first Page of pdf ")

            assert processCharge in firstPage, "processCharge is matched with CHARGES Section in first Page of pdf"

        except:
            try:
                if processChargeRs in firstPage:
                    print(f" *** 'processChargeRs' :'{processChargeRs}' is matched with CHARGES Section in first Page of pdf *** ")
                else:
                    print(f"Exception :: 'processChargeRs' :'{processChargeRs}' is not matched with CHARGES Section in first Page of pdf ")

                assert processChargeRs in firstPage, "processChargeRs is matched with CHARGES Section in first Page of pdf"

            except:
                if processChargeRs2 in firstPage:
                    print(
                        f" *** 'processChargeRs2' :'{processChargeRs2}' is matched with CHARGES Section in first Page of pdf *** ")
                else:
                    print(
                        f"Error :: 'processChargeRs2' :'{processChargeRs2}' is not matched with CHARGES Section in first Page of pdf ")

                assert processChargeRs2 in firstPage, "processChargeRs2 is matched with CHARGES Section in first Page of pdf"




        #Document Charges @1%
        docChargFloat = (loanAmountInt/100) * 1
        docChargInt = math.ceil((loanAmountInt / 100) * 1)

        documentCharges = "₹" + str(docChargFloat) + "0"
        documentCharges2 = "₹" + str(docChargInt)

        # print("documentCharges2::",documentCharges2)
        #
        try:
            if documentCharges in firstPage:
                print(f" *** 'documentCharges' :'{documentCharges}' is matched with CHARGES Section in first Page of pdf *** ")
            else:
                print(f"Exception :: 'documentCharges' :'{documentCharges}' is not matched with CHARGES Section in first Page of pdf ")

            assert documentCharges in firstPage, "is matched with CHARGES Section in first Page of pdf"

        except:
            if documentCharges2 in firstPage:
                print(
                    f" *** 'documentCharges2' :'{documentCharges2}' is matched with CHARGES Section in first Page of pdf *** ")
            else:
                print(
                    f"Error :: 'documentCharges2' :'{documentCharges2}' is not matched with CHARGES Section in first Page of pdf ")

            assert documentCharges2 in firstPage, "is matched with CHARGES Section in first Page of pdf"



        # 9% SGST is inclusive As specified by Government of India
        onlineConvenienceFees = 200
        riskAssessmentFees = 200
        sgstFloat = ((processChargeInt + docChargFloat + onlineConvenienceFees + riskAssessmentFees) / 100) * 9
        sgst = "₹" + str(round(sgstFloat,2))
        sgst2 = "₹" + str(round(sgstFloat,1))


        try:
            if sgst in firstPage:
                print(f" *** 'sgst' :'{sgst}' is matched with CHARGES Section in first Page of pdf *** ")
            else:
                print(f" *** 'sgst' :'{sgst}' is not matched with CHARGES Section in first Page of pdf *** ")

            assert sgst in firstPage, "is matched with CHARGES Section in first Page of pdf"

        except:
            if sgst2 in firstPage:
                print(f" *** 'sgst2' :'{sgst2}' is matched with CHARGES Section in first Page of pdf *** ")
            else:
                print(f"Error :: 'sgst2' :'{sgst2}' is not matched with CHARGES Section in first Page of pdf ")

            assert sgst2 in firstPage, "is matched with CHARGES Section in first Page of pdf"


        # 9% CGST is inclusive As specified by Government of India
        # onlineConvenienceFees = 150
        cgstFloat = ((processChargeInt + docChargFloat + onlineConvenienceFees + riskAssessmentFees) / 100) * 9
        cgst = "₹" + str(round(cgstFloat,2))
        cgst2 = "₹" + str(round(cgstFloat, 1))

        try:
            if cgst in firstPage:
                print(f" *** 'cgst' :'{cgst}' is matched with CHARGES Section in first Page of pdf *** ")
            else:
                print(f" *** 'cgst' :'{cgst}' is not matched with CHARGES Section in first Page of pdf *** ")
            assert cgst in firstPage, "is matched with CHARGES Section in first Page of pdf"


        except:
            if cgst2 in firstPage:
                print(f" *** 'cgst2' :'{cgst2}' is matched with CHARGES Section in first Page of pdf *** ")
            else:
                print(f"Error :: 'cgst2' :'{cgst2}' is not matched with CHARGES Section in first Page of pdf ")
            assert cgst2 in firstPage, "is matched with CHARGES Section in first Page of pdf"

        #

        #Online convenience fees
        onlineConvenienceFeesString = "₹" + str(onlineConvenienceFees)
        if onlineConvenienceFeesString in firstPage:
            print(f" *** 'onlineConvenienceFeesString' :'{onlineConvenienceFeesString}' is inside CHARGES Section of first Page of pdf *** ")
        else:
            print(f"Error :: 'onlineConvenienceFeesString' :'{onlineConvenienceFeesString}' is not inside CHARGES Section of first Page of pdf ")

        assert onlineConvenienceFeesString in firstPage, "is inside CHARGES Section of first Page of pdf"


        #Cheque / ECS / SI Return charges
        chequeBounceCharge = "₹500"
        if chequeBounceCharge in firstPage:
            print(f" *** 'chequeBounceCharge' :'{chequeBounceCharge}' is inside CHARGES Section of first Page of pdf *** ")
        else:
            print(f"Error :: 'chequeBounceCharge' :'{chequeBounceCharge}' is not inside CHARGES Section of first Page of pdf ")

        assert chequeBounceCharge in firstPage, "is inside CHARGES Section of first Page of pdf"


        #Default Interest / Late Payment charges (per day)
        latePaymentChargePerDay = flotLIPD * 2
        latePaymentChargePerDayString = str(latePaymentChargePerDay) + "%"


        if latePaymentChargePerDayString in firstPage:
            print(f" *** 'latePaymentChargePerDayString' :'{latePaymentChargePerDayString}' is matched and is inside CHARGES Section of first Page of pdf *** ")
        else:
            print(f"Error :: 'latePaymentChargePerDayString' :'{latePaymentChargePerDayString}' is not matched and not inside CHARGES Section of first Page of pdf ")

        assert latePaymentChargePerDayString in firstPage, "is matched and within CHARGES Section of first Page of pdf"


        # Default Interest / Late Payment charges (per annual)
        latePaymentChargePerAnnual = round(loanIntPerAnnum * 2,3)
        latePaymentChargePerAnnualInt = int(round(loanIntPerAnnum * 2,3))

        latePaymentChargePerAnnualString = str(latePaymentChargePerAnnual) + "00%"
        latePaymentChargePerAnnualString2 = str(latePaymentChargePerAnnual) + "0%"
        latePaymentChargePerAnnualString3 = str(latePaymentChargePerAnnualInt) + "%"

        try:
            if latePaymentChargePerAnnualString in firstPage:
                print(f" *** 'latePaymentChargePerAnnualString' :'{latePaymentChargePerAnnualString}' is matched with CHARGES Section in first Page of pdf *** ")
            else:
                print(f"Exception :: 'latePaymentChargePerAnnualString' :'{latePaymentChargePerAnnualString}' is not matched with CHARGES Section in first Page of pdf ")

            assert latePaymentChargePerAnnualString in firstPage, "is matched with CHARGES Section in first Page of pdf"

        except:
            try:
                if latePaymentChargePerAnnualString2 in firstPage:
                    print(
                        f" *** 'latePaymentChargePerAnnualString2' :'{latePaymentChargePerAnnualString2}' is matched with CHARGES Section in first Page of pdf *** ")
                else:
                    print(
                        f"Exception :: 'latePaymentChargePerAnnualString2' :'{latePaymentChargePerAnnualString2}' is not matched with CHARGES Section in first Page of pdf ")

                assert latePaymentChargePerAnnualString2 in firstPage, "is matched with CHARGES Section in first Page of pdf"

            except:
                if latePaymentChargePerAnnualString3 in firstPage:
                    print(
                        f" *** 'latePaymentChargePerAnnualString3' :'{latePaymentChargePerAnnualString3}' is matched with CHARGES Section in first Page of pdf *** ")
                else:
                    print(
                        f"Error :: 'latePaymentChargePerAnnualString3' :'{latePaymentChargePerAnnualString3}' is not matched with CHARGES Section in first Page of pdf ")

                assert latePaymentChargePerAnnualString3 in firstPage, "is matched with CHARGES Section in first Page of pdf"





        '''LETTER OF SANCTION TO THE BORROWER'''

        # Total amount to be paid
        totalCost = driver.find_element(By.XPATH,"//div[contains(@class,'font-weight-bold numbers mobile-text')]").text

        if totalCost in thirdPage:
            print(f" *** 'totalCost' :'{totalCost}' is matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf *** ")
        else:
            print(f"Error :: 'totalCost' :'{totalCost}' is not matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf ")

        assert totalCost in thirdPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf"


        #TOTAL PERIOD
        time.sleep(1)
        loanDurationInDays = loanDurInDays + " days"
        totalPeriod = loanDurationInDays

        if totalPeriod in thirdPage:
            print(f" *** 'totalPeriod' :'{totalPeriod}' is matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf *** ")
        else:
            print(f"Error :: 'totalPeriod' :'{totalPeriod}' is not matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf ")

        assert totalPeriod in thirdPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf"


        #COMMENCING FROM
        # LoanDisbursementDate = driver.find_element(By.XPATH,"//tr[contains(@class,'mat-row cdk-row loan-history-row bg-greywhite ng-star-inserted')]//td[6]//div").text
        LoanDisbursementDate = driver.find_element(By.XPATH,"(//div[@class='mobile-text fnt-size-12 ng-star-inserted'])[3]").text
        commencingFrom = LoanDisbursementDate.replace('/','-')
        time.sleep(1)

        try:
            if commencingFrom in thirdPage:
                print(f" *** 'commencingFrom' :'{commencingFrom}' is matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf *** ")
            else:
                print(f"Exception :: 'commencingFrom' :'{commencingFrom}' is not matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf ")

            assert commencingFrom in thirdPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf"

        except:
            if 'Date of Signing' in firstPage:
                index1 = firstPage.index('Date of Signing')
                index2 = firstPage.index('Name of Borrower')
                text = firstPage[index1 + 28:index2]
                print(f"By pdf :: {text}")



        # ONLINE CONVENIENCE CHARGES
        onlineConvCharge = 200
        onlineConvChargeString = "₹200"

        if onlineConvChargeString in thirdPage:
            print(f" *** 'onlineConvChargeString' :'{onlineConvChargeString}' is inside LETTER OF SANCTION TO THE BORROWER Section in third page of pdf *** ")
        else:
            print(f"Error :: 'onlineConvChargeString' :'{onlineConvChargeString}' is not inside LETTER OF SANCTION TO THE BORROWER Section in third page of pdf ")

        assert onlineConvChargeString in thirdPage, "is inside LETTER OF SANCTION TO THE BORROWER Section in third page of pdf"


        # #INSURANCE CHARGES
        try:
            insCharg = float(insurancePremAmount[1:])

        except:
            insCharg2 = 0

        #DISBURSEMENT

        try:
            try:
                disburse = loanAmountInt - (processChargeInt + docChargFloat + riskAssessmentFees + onlineConvCharge + sgstFloat + cgstFloat + insCharg)
                disFloat = str(math.ceil(disburse))
                disbursement = "₹" + disFloat[0:2] + "," + disFloat[2:]

                if disbursement in thirdPage:
                    print(f" *** 'disbursement' :'{disbursement}' is matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf *** ")
                else:
                    print(f"Exception :: 'disbursement' :'{disbursement}' is not matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf ")

                assert disbursement in thirdPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf"

            except:
                try:
                    disburse = loanAmountInt - (processChargeInt + docChargFloat + riskAssessmentFees + onlineConvCharge + sgstFloat + cgstFloat + insCharg)
                    disFloat = str(math.ceil(disburse))[:8]

                    disbursement = "₹" + disFloat[0:2] + "," + disFloat[2:]

                    if disbursement in thirdPage:
                        print(
                            f" *** 'disbursement' :'{disbursement}' is matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf *** ")
                    else:
                        print(
                            f"Exception :: 'disbursement' :'{disbursement}' is not matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf ")

                    assert disbursement in thirdPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf"

                except:
                    try:

                        disburse = loanAmountInt - (processChargeInt + docChargFloat + riskAssessmentFees + onlineConvCharge + sgstFloat + cgstFloat + insCharg2)
                        disFloat = str(math.ceil(disburse-2))
                        disbursement = "₹" + disFloat[0:2] + "," + disFloat[2:]
                        if disbursement in thirdPage:
                            print(
                                f" *** 'disbursement' :'{disbursement}' is matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf *** ")
                        else:
                            print(
                                f"Exception :: 'disbursement' :'{disbursement}' is not matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf ")


                        assert disbursement in thirdPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf"
                    except:
                        try:

                            disburse = loanAmountInt - (
                                        processChargeInt + docChargFloat + riskAssessmentFees + onlineConvCharge + sgstFloat + cgstFloat + insCharg2)
                            disFloat = str(math.ceil(disburse))
                            disbursement = "₹" + disFloat[0:2] + "," + disFloat[2:]
                            if disbursement in thirdPage:
                                print(
                                    f" *** 'disbursement' :'{disbursement}' is matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf *** ")
                            else:
                                print(
                                    f"Exception :: 'disbursement' :'{disbursement}' is not matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf ")

                            assert disbursement in thirdPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf"


                        except:
                            disburse = loanAmountInt - (processChargeInt + docChargFloat + riskAssessmentFees + onlineConvCharge + sgstFloat + cgstFloat + insCharg2)
                            disFloat = str(math.ceil(disburse-1))
                            disbursement = "₹" + disFloat[0:1] + "," + disFloat[1:]
                            if disbursement in thirdPage:
                                print(
                                    f" *** 'disbursement' :'{disbursement}' is matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf *** ")
                            else:
                                print(
                                    f"Error :: 'disbursement' :'{disbursement}' is not matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf ")

                            assert disbursement in thirdPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section in third page of pdf"

        except:
            pass


        '''SECURITY DOCUMENTS'''

        #Sanction Days
        sanctionDays = "10 days"
        if sanctionDays in fourthPage:
            print(f" *** 'sanctionDays' :'{sanctionDays}' is matched with SECURITY DOCUMENTS section in fourth page of pdf *** ")
        else:
            print(f"Error :: 'sanctionDays' :'{sanctionDays}' is not matched with SECURITY DOCUMENTS section in fourth page of pdf ")

        assert sanctionDays in fourthPage, "is matched with SECURITY DOCUMENTS section in fourth page of pdf"


        #Penal interest per day
        penalInterestPerDay = latePaymentChargePerDayString
        if penalInterestPerDay in fourthPage:
            print(f" *** 'penalInterestPerDay' :'{penalInterestPerDay}' is matched with SECURITY DOCUMENTS section in fourth Page of pdf *** ")
        else:
            print(f"Error :: 'penalInterestPerDay' :'{penalInterestPerDay}' is not matched with SECURITY DOCUMENTS section in fourth Page of pdf ")

        assert penalInterestPerDay in fourthPage, "penalInterestPerDay is matched with SECURITY DOCUMENTS section in fourth Page of pdf"

        # Penal interest per annum
        try:
            penalInterestPerAnnum = latePaymentChargePerAnnualString
            if penalInterestPerAnnum in fourthPage:
                print(f" *** 'penalInterestPerAnnum' :'{penalInterestPerAnnum}' is matched with SECURITY DOCUMENTS section in fourth Page of pdf *** ")
            else:
                print(f"Exception :: 'penalInterestPerAnnum' :'{penalInterestPerAnnum}' is not matched with SECURITY DOCUMENTS section in fourth Page of pdf ")

            assert penalInterestPerAnnum in fourthPage, "penalInterestPerAnnum is matched with SECURITY DOCUMENTS section in fourth Page of pdf"

        except:
            try:
                penalInterestPerAnnum2 = latePaymentChargePerAnnualString2
                if penalInterestPerAnnum2 in fourthPage:
                    print(
                        f" *** 'penalInterestPerAnnum2' :'{penalInterestPerAnnum2}' is matched with SECURITY DOCUMENTS section in fourth Page of pdf *** ")
                else:
                    print(
                        f"Exception :: 'penalInterestPerAnnum2' :'{penalInterestPerAnnum2}' is not matched with SECURITY DOCUMENTS section in fourth Page of pdf ")

                assert penalInterestPerAnnum2 in fourthPage, "penalInterestPerAnnum2 is matched with SECURITY DOCUMENTS section in fourth Page of pdf"
            except:
                penalInterestPerAnnum3 = latePaymentChargePerAnnualString3
                if penalInterestPerAnnum3 in fourthPage:
                    print(
                        f" *** 'penalInterestPerAnnum3' :'{penalInterestPerAnnum3}' is matched with SECURITY DOCUMENTS section in fourth Page of pdf *** ")
                else:
                    print(
                        f"Error :: 'penalInterestPerAnnum3' :'{penalInterestPerAnnum3}' is not matched with SECURITY DOCUMENTS section in fourth Page of pdf ")

                assert penalInterestPerAnnum3 in fourthPage, "penalInterestPerAnnum3 is matched with SECURITY DOCUMENTS section in fourth Page of pdf"

        #Name of Borrower in security document
        try:
            if profileName in fourthPage:
                print(f" *** 'profileName':'{profileName}' is matched with security document section in fourth Page of pdf *** ")
            else:
                print(f"Exception :: 'profileName':'{profileName}' is not matched with security document section in fourth Page of pdf ")

            assert profileName in fourthPage, "profileName is matched with security document section in fourth Page of pdf"

        except:
            if 'Name of Borrower' in firstPage:
                index1 = firstPage.index('Name of Borrower')
                index2 = firstPage.index('NBFC NameChinmay Finlease')
                text = firstPage[index1 + 16:index2]
                print(f"Name by pdf module :: {text}")


        '''Proof of identity'''
        adhar = driver.find_element(By.ID,"aadhaar").text


        if adhar in seventhPage:
            print(
                f" *** 'adhar':'{adhar}' is matched with Proof of identity section of seventh Page of pdf *** ")
        else:
            print(
                f"Exception :: 'adhar':'{adhar}' is not matched with Proof of identity section of seventh Page of pdf ")

        assert adhar in seventhPage, "adhar is matched with Proof of identity section of seventh Page of pdf"


        try:
            if profileName in seventhPage:
                print(f" *** 'profileName':'{profileName}' is matched with Proof of identity section of seventh Page of pdf *** ")
            else:
                print(f"Exception :: 'profileName':'{profileName}' is not matched with Proof of identity section of seventh Page of pdf ")

            assert profileName in seventhPage, "profileName is matched with Proof of identity section of seventh Page of pdf"

        except:
            if 'Name of Borrower' in firstPage:
                index1 = firstPage.index('Name of Borrower')
                index2 = firstPage.index('NBFC NameChinmay Finlease')
                text = firstPage[index1 + 16:index2]
                print(f"Name by pdf module :: {text}")


        gender = driver.find_element(By.ID,"gender").text


        if gender in seventhPage:
            print(
                f" *** 'gender':'{gender}' is matched with Proof of identity section of seventh Page of pdf *** ")
        else:
            print(
                f"Exception :: 'gender':'{gender}' is not matched with Proof of identity section of seventh Page of pdf ")

        assert gender in seventhPage, "gender is matched with Proof of identity section of seventh Page of pdf"



        '''LOAN AGREEMENT'''
        #Name of Borrower in loan agreement
        try:
            if profileName in eighthPage:
                print(f" *** 'profileName':'{profileName}' is matched with LOAN AGREEMENT section of eighth Page of pdf *** ")
            else:
                print(f"Exception :: 'profileName':'{profileName}' is not matched with LOAN AGREEMENT section of eighth Page of pdf ")

            assert profileName in eighthPage, "profileName is matched with LOAN AGREEMENT section of eighth Page of pdf"
        except:
            if 'Name of Borrower' in firstPage:
                index1 = firstPage.index('Name of Borrower')
                index2 = firstPage.index('NBFC NameChinmay Finlease')
                text = firstPage[index1 + 16:index2]
                print(f"Name by pdf module :: {text}")


        # Email

        # emailS = driver.find_element(By.XPATH,"(//div[@class='fnt-size-12 font-weight-bold d-flex flex-row word-wrap mobile-text'])[1]").text
        emailS = driver.find_element(By.ID,"emailId").text
        time.sleep(2)


        try:
            if emailS in eighthPage:
                print(f" *** 'email' :'{emailS}' is matched with LOAN AGREEMENT section of eighth Page of pdf *** ")
            else:
                print(f"Exception :: 'email' :'{emailS}' is not matched with LOAN AGREEMENT section of eighth Page of pdf ")

            assert emailS in eighthPage, "email is matched with LOAN AGREEMENT section of eighth Page of pdf"

        except:
            eindex = emailS.index("View")
            email = emailS[:eindex - 1]

            if email in eighthPage:
                print(f" *** 'email' :'{email}' is matched with LOAN AGREEMENT of eighth Page of pdf *** ")
            else:
                print(f"Exception :: 'email' :'{email}' is not matched with LOAN AGREEMENT of eighth Page of pdf ")

            assert email in eighthPage, "email is matched with LOAN AGREEMENT in eighth Page of pdf"


        # PAN number
        # pan = driver.find_element(By.XPATH,"//div[contains(@class,'basic-details d-flex flex-row basic-info-card align-items-center justify-content-between mt-2')][2]//div[2]").text
        pan = driver.find_element(By.ID,"PAN").text
        time.sleep(1)

        if pan in eighthPage:
            print(f" *** 'pan' :'{pan}' is matched with LOAN AGREEMENT in eighth Page of pdf *** ")
        else:
            print(f"Error :: 'pan' :'{pan}' is not matched with LOAN AGREEMENT in eighth Page of pdf ")

        assert pan in eighthPage, "pan is matched with LOAN AGREEMENT in eighth Page of pdf"


        # loan amount
        lA = approvedAmount
        loanAmountstr = lA.replace("/-","")

        lA2 = approvedAmount2
        loanAmountstr2 = lA2.replace("/-","")


        try:
            if loanAmountstr in eighthPage:
                print(f" *** 'loanAmountstr' :'{loanAmountstr}' is matched with LOAN AGREEMENT in eighth Page of pdf *** ")
            else:
                print(f"Exception :: 'loanAmountstr' :'{loanAmountstr}' is not matched with LOAN AGREEMENT in eighth Page of pdf ")

            assert loanAmountstr in eighthPage, "loanAmountstr is matched with LOAN AGREEMENT in eighth Page of pdf"
        except:
            if loanAmountstr2 in eighthPage:
                print(
                    f" *** 'loanAmountstr2' :'{loanAmountstr2}' is matched with LOAN AGREEMENT in eighth Page of pdf *** ")
            else:
                print(
                    f"Error :: 'loanAmountstr2' :'{loanAmountstr2}' is not matched with LOAN AGREEMENT in eighth Page of pdf ")

            assert loanAmountstr2 in eighthPage, "loanAmountstr2 is matched with LOAN AGREEMENT in eighth Page of pdf"


        # loan period
        if loanDurationInDays in eighthPage:
            print(f" *** 'loanDurationInDays' :'{loanDurationInDays}' is matched with LOAN AGREEMENT in eighth Page of pdf *** ")
        else:
            print(f"Error :: 'loanDurationInDays' :'{loanDurationInDays}' is not matched with LOAN AGREEMENT in eighth Page of pdf ")

        assert loanDurationInDays in eighthPage, "loanDurationInDays is matched with LOAN AGREEMENT in eighth Page of pdf"


        # loan interest
        #per day

        try:
            if loanInterestPerDay in eighthPage:
                print(f" *** 'loanInterestPerDay' :'{loanInterestPerDay}' is matched with LOAN AGREEMENT in eighth Page of pdf *** ")
            else:
                print(f"Exception :: 'loanInterestPerDay' :'{loanInterestPerDay}' is not matched with LOAN AGREEMENT in eighth Page of pdf ")

            assert loanInterestPerDay in eighthPage, "loanInterestPerDay is matched with LOAN AGREEMENT in eighth Page of pdf"

        except:
            try:
                if loanInterestPerDay2 in eighthPage:
                    print(
                        f" *** 'loanInterestPerDay2' :'{loanInterestPerDay2}' is matched with LOAN AGREEMENT in eighth Page of pdf *** ")
                else:
                    print(
                        f"Exception :: 'loanInterestPerDay2' :'{loanInterestPerDay2}' is not matched with LOAN AGREEMENT in eighth Page of pdf ")

                assert loanInterestPerDay2 in eighthPage, "loanInterestPerDay is matched with LOAN AGREEMENT in eighth Page of pdf"

            except:

                if loanInterestPerDay3 in eighthPage:
                    print(
                        f" *** 'loanInterestPerDay3' :'{loanInterestPerDay3}' is matched with LOAN AGREEMENT in eighth Page of pdf *** ")
                else:
                    print(
                        f"Error :: 'loanInterestPerDay3' :'{loanInterestPerDay3}' is not matched with LOAN AGREEMENT in eighth Page of pdf ")

                assert loanInterestPerDay3 in eighthPage, "loanInterestPerDay3 is matched with LOAN AGREEMENT in eighth Page of pdf"

        #per annum

        try:
            if loanIntPerAnnumStr in eighthPage:
                print(f" *** 'loanIntPerAnnumStr' :'{loanIntPerAnnumStr}%' is matched with LOAN DETAILS in eighth Page of pdf *** ")
            else:
                print(f"Exception :: 'loanIntPerAnnumStr' :'{loanIntPerAnnumStr}%'  is not matched with LOAN DETAILS in eighth Page of pdf ")

            assert loanIntPerAnnumStr in eighthPage, "loanIntPerAnnumStr is matched with LOAN DETAILS in eighth Page of pdf"
        except:
            if loanIntPerAnnumStr2 in eighthPage:
                print(f" *** 'loanIntPerAnnumStr2' :'{loanIntPerAnnumStr2}%' is matched with LOAN DETAILS in eighth Page of pdf *** ")
            else:
                print(f"Error :: 'loanIntPerAnnumStr2' :'{loanIntPerAnnumStr2}%'  is not matched with LOAN DETAILS in eighth Page of pdf ")

            assert loanIntPerAnnumStr2 in eighthPage, "loanIntPerAnnumStr2 is matched with LOAN DETAILS in eighth Page of pdf"



        # penalty interest per day

        if latePaymentChargePerDayString in eighthPage:
            print(f" *** 'latePaymentChargePerDayString' :'{latePaymentChargePerDayString}' is matched with LOAN AGREEMENT in eighth Page of pdf *** ")
        else:
            print(f"Error :: 'latePaymentChargePerDayString' :'{latePaymentChargePerDayString}' is not matched with LOAN AGREEMENT in eighth Page of pdf ")

        assert latePaymentChargePerDayString in eighthPage, "latePaymentChargePerDayString is matched with LOAN AGREEMENT in eighth Page of pdf"

        # per annum
        try:
            if latePaymentChargePerAnnualString in eighthPage:
                print(f" *** 'latePaymentChargePerAnnualString' :'{latePaymentChargePerAnnualString}' is matched with LOAN AGREEMENT in eighth Page of pdf *** ")
            else:
                print(f"Exception :: 'latePaymentChargePerAnnualString' :'{latePaymentChargePerAnnualString}' is not matched with LOAN AGREEMENT in eighth Page of pdf ")

            assert latePaymentChargePerAnnualString in eighthPage, "latePaymentChargePerAnnualString is matched with LOAN AGREEMENT in eighth Page of pdf"

        except:
            try:
                if latePaymentChargePerAnnualString2 in eighthPage:
                    print(
                        f" *** 'latePaymentChargePerAnnualString2' :'{latePaymentChargePerAnnualString2}' is matched with LOAN AGREEMENT in eighth Page of pdf *** ")
                else:
                    print(
                        f"Exception :: 'latePaymentChargePerAnnualString2' :'{latePaymentChargePerAnnualString2}' is not matched with LOAN AGREEMENT in eighth Page of pdf ")

                assert latePaymentChargePerAnnualString2 in eighthPage, "latePaymentChargePerAnnualString2 is matched with LOAN AGREEMENT in eighth Page of pdf"
            except:
                if latePaymentChargePerAnnualString3 in eighthPage:
                    print(
                        f" *** 'latePaymentChargePerAnnualString3' :'{latePaymentChargePerAnnualString3}' is matched with LOAN AGREEMENT in eighth Page of pdf *** ")
                else:
                    print(
                        f"Error :: 'latePaymentChargePerAnnualString3' :'{latePaymentChargePerAnnualString3}' is not matched with LOAN AGREEMENT in eighth Page of pdf ")

                assert latePaymentChargePerAnnualString3 in eighthPage, "latePaymentChargePerAnnualString3 is matched with LOAN AGREEMENT in eighth Page of pdf"

        '''Borrower Name in ninth page'''

        try:
            if profileName in eleventhPage:
                print(f" *** 'profileName':'{profileName}' is matched with witness in eleventh Page of pdf *** ")
            else:
                print(f"Exception :: 'profileName':'{profileName}' is not matched with witness in eleventh Page of pdf ")

            assert profileName in eleventhPage, "profileName is matched with witness in eleventh Page of pdf"

        except:
            if 'Name of Borrower' in firstPage:
                index1 = firstPage.index('Name of Borrower')
                index2 = firstPage.index('NBFC NameChinmay Finlease')
                text = firstPage[index1 + 16:index2]
                print(f"Name by pdf module :: {text}")


        #
