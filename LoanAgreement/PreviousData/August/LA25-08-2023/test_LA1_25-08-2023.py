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


# JSON reader
file = open("input_25-08-2023.json")
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
ninthPage = reader.pages[8].extract_text()


class TestDashRepo:
    @pytest.fixture()
    def setup_teardown(self):
        global driver

        ser = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service = ser)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://lendittfinserve.com/lenditt/#/dashboard") # url
        # time.sleep(1)
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys(email) #email
        # time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/app-root/app-auth/div/div[2]/div/div/form/div/button").click()
        # time.sleep(1)
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password) #password
        # time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/app-root/app-auth/div/div[2]/div/div/form/div[2]/button").click()
        # time.sleep(1)
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys(otp) #otp
        # time.sleep(1)
        element = driver.find_element(By.XPATH, "/html/body/app-root/app-auth/div/div[2]/div/div/form/div[2]/button")
        # time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        # time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > app-root > app-auth > div > div:nth-child(2) > div > div > form > div.submit-btn.margin-top-bottom.d-flex.justify-content-center.ng-star-inserted > button").click()
        time.sleep(1)
        yield
        time.sleep(1)
        driver.close()
        driver.quit()
        print("test execution completed")


    def test_keyFactStatement(self, setup_teardown):
        driver.find_element(By.ID, "mainSearch").send_keys(loanID)  #
        time.sleep(2)
        driver.find_element(By.XPATH, "(//div[contains(@class,'search-text-master')])").click()  #click user
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(1)


        '''SCHEDULE-CUM-KEY FACT STATEMENT'''

        # Name of Borrower
        profileName = driver.find_element(By.XPATH,"(//div[contains(@class,'profile-details')])/div[1]").text
        time.sleep(2)
        print(f"### 'profileName':'{profileName}' ###")
        time.sleep(1)

        try:
            if profileName in firstPage:
                print(f" *** 'profileName':'{profileName}' is matched with KEY FACT STATEMENT first Page of pdf *** ")
            else:
                print(f"Exception :: 'profileName':'{profileName}' is not matched with KEY FACT STATEMENT first Page of pdf ")

            assert profileName in firstPage, "profileName is matched with KEY FACT STATEMENT first Page of pdf"

        except:
            if 'Name of Borrower' in firstPage:
                index1 = firstPage.index('Name of Borrower')
                index2 = firstPage.index('NBFC NameChinmay Finlease')
                text = firstPage[index1 + 16:index2]
                print(f"Name by pdf module :: {text}")



        # #loanId
        loanId = driver.find_element(By.XPATH,"//a[contains(@style,'text-decoration: none;')][1]").text
        time.sleep(1)
        if loanId in firstPage:
            print(f" *** 'loanId' :'{loanId}' is matched with KEY FACT STATEMENT first Page of pdf *** ")
        else:
            print(f"Error :: 'loanId' :'{loanId}' is not matched with KEY FACT STATEMENT first Page of pdf ")

        assert loanId in firstPage, "loanId is matched with KEY FACT STATEMENT first Page of pdf"


        # Date of Signing
        try:
            loanAppDate = driver.find_element(By.XPATH, "(//div[@class='mobile-text fnt-size-12 ng-star-inserted'])[2]").text
            time.sleep(1)
            LoanApplicationDate = loanAppDate.replace('/','-')

            if LoanApplicationDate in firstPage:
                print(f" *** 'LoanApplicationDate' :'{LoanApplicationDate}' is matched with KEY FACT STATEMENT first Page of pdf *** ")

            assert LoanApplicationDate in firstPage, "LoanApplicationDate is matched with KEY FACT STATEMENT first Page of pdf"

        except:
            loanAppDate = driver.find_element(By.XPATH,"(//div[@class='mobile-text fnt-size-12 ng-star-inserted'])[3]").text
            time.sleep(1)
            LoanApplicationDate = loanAppDate.replace('/', '-')

            if LoanApplicationDate in firstPage:
                print(f" *** 'LoanApplicationDate' :'{LoanApplicationDate}' is matched with KEY FACT STATEMENT first Page of pdf *** ")
            else:
                print(f"Error :: 'LoanApplicationDate' :'{LoanApplicationDate}' is not matched with KEY FACT STATEMENT first Page of pdf ")

            assert LoanApplicationDate in firstPage, "LoanApplicationDate is matched with KEY FACT STATEMENT first Page of pdf"



        '''LOAN DETAILS'''
        # # Loan Amount
        apprAmount = driver.find_element(By.XPATH,"(//div[@class='mobile-text fnt-size-12 ng-star-inserted'][contains(text(),'₹ 17,500')])[1]").text
        time.sleep(2)
        lSpace = apprAmount.replace(" ","")
        approvedAmount = lSpace + '.00/-'

        if approvedAmount in firstPage:
            print(f" *** 'approvedAmount' :'{approvedAmount}' is matched with LOAN DETAILS first Page of pdf *** ")
        else:
            print(f"Error :: 'approvedAmount' :'{approvedAmount}' is not matched with LOAN DETAILS first Page of pdf ")

        assert approvedAmount in firstPage, "approvedAmount is matched with LOAN DETAILS first Page of pdf"


        # Interest Rate (per Day)
        loanIntPerDay = driver.find_element(By.XPATH,"//td[contains(@class,'mat-cell cdk-cell mobile-text fnt-size-12 cdk-column-loanInterest mat-column-loanInterest ng-star-inserted')]").text
        time.sleep(1)
        loanInterestPerDay = loanIntPerDay.replace(" %","0%")
        if loanInterestPerDay in firstPage:
            print(f" *** 'loanInterestPerDay' :'{loanInterestPerDay}' is matched with LOAN DETAILS first Page of pdf *** ")
        else:
            print(f"Error :: 'loanInterestPerDay' :'{loanInterestPerDay}' is not matched with LOAN DETAILS first Page of pdf ")

        assert loanInterestPerDay in firstPage, "loanInterestPerDay is matched with LOAN DETAILS first Page of pdf"


        # # Interest Rate (per Annum)
        strLIPD = loanIntPerDay.replace(" %","")
        flotLIPD = float(strLIPD)
        loanIntPerAnnum = flotLIPD * 365
        loanIntPerAnnumInt = int(loanIntPerAnnum)
        loanIntPerAnnumStr = str(loanIntPerAnnumInt)

        if loanIntPerAnnumStr in firstPage:
            print(f" *** 'loanIntPerAnnumStr' :'{loanIntPerAnnumStr}%' is matched with LOAN DETAILS first Page of pdf *** ")
        else:
            print(f"Error :: 'loanIntPerAnnumStr' :'{loanIntPerAnnumStr}%'  is not matched with LOAN DETAILS first Page of pdf ")

        assert loanIntPerAnnumStr in firstPage, "loanIntPerAnnumStr is matched with LOAN DETAILS first Page of pdf"


        # # Insurance premium amount
        inPremAmount = driver.find_element(By.XPATH,"//td[contains(@class,'mat-cell cdk-cell cdk-column-insuranceAmount')]//div").text
        time.sleep(1)
        insurancePremAmount = inPremAmount.replace(" ","")
        if insurancePremAmount in firstPage:
            print(f" *** 'insurancePremAmount' :'{insurancePremAmount}' is matched with LOAN DETAILS first Page of pdf *** ")
        else:
            print(f"Error :: 'insurancePremAmount' :'{insurancePremAmount}' is not matched with LOAN DETAILS first Page of pdf ")

        assert insurancePremAmount in firstPage, "insurancePremAmount is matched with LOAN DETAILS first Page of pdf"

        #
        # # # Loan Tenure
        loanDurInDays = driver.find_element(By.XPATH,"//td[contains(@class,'mat-cell cdk-cell mobile-text fnt-size-12 cdk-column-loanDuration mat-column-loanDuration ng-star-inserted')]").text
        time.sleep(1)
        loanDurationInDays = loanDurInDays + " Days"
        if loanDurationInDays in firstPage:
            print(f" *** 'loanDurationInDays' :'{loanDurationInDays}' is matched with LOAN DETAILS first Page of pdf *** ")
        else:
            print(f"Error :: 'loanDurationInDays' :'{loanDurationInDays}' is not matched with LOAN DETAILS first Page of pdf ")

        assert loanDurationInDays in firstPage, "loanDurationInDays is matched with LOAN DETAILS first Page of pdf"

        #
        # # Loan Start Date
        loanDisbDate = driver.find_element(By.XPATH,"//td[contains(@class,'mat-cell cdk-cell cdk-column-loanStartDate mat-column-loanStartDate ng-star-inserted')]//div").text
        time.sleep(1)
        loanDisbursedDate = loanDisbDate.replace("/","-")
        if loanDisbursedDate in firstPage:
            print(f" *** 'loanDisbursedDate' :'{loanDisbursedDate}' is matched with LOAN DETAILS first Page of pdf *** ")
        else:
            print(f"Error :: 'loanDisbursedDate' :'{loanDisbursedDate}' is not matched with LOAN DETAILS first Page of pdf ")

        assert loanDisbursedDate in firstPage, "loanDisbursedDate is matched with LOAN DETAILS first Page of pdf"


        # Loan End Date
        loanStartDate = datetime.strptime(loanDisbursedDate,"%d-%m-%Y")
        loanEndDateTimeFromY = loanStartDate + timedelta(days=int(loanDurInDays)-1)
        time.sleep(1)
        loanEndDateFromD = datetime.strftime(loanEndDateTimeFromY,'%d-%m-%Y')
        loanEndDate = str(loanEndDateFromD).split(" ")[0]
        time.sleep(1)
        if loanEndDate in firstPage:
            print(f" *** 'loanEndDate' :'{loanEndDate}' is matched with LOAN DETAILS first Page of pdf *** ")
        else:
            print(f"Error :: 'loanEndDate' :'{loanEndDate}' is not matched with LOAN DETAILS first Page of pdf ")

        assert loanEndDate in firstPage, "loanEndDate is matched with LOAN DETAILS first Page of pdf"


        '''CHARGES (All charges are non-refundable & applicable post disbursement of loan)'''
        rmLoanAmInt = apprAmount.replace("₹ ","")
        rmChLoanAmInt = rmLoanAmInt.replace(",","")
        loanAmountInt = int(rmChLoanAmInt)

        # #Processing Charges @6.5%
        processChargeInt = (loanAmountInt/100) * 6.5
        processChargeString = format(processChargeInt, '.2f')
        processChargeRs = "₹" + processChargeString
        processCharge =  processChargeRs[0] + processChargeRs[1] + "," + processChargeRs[2:]

        if processCharge in firstPage:
            print(f" *** 'processCharge' :'{processCharge}' is matched and with CHARGES Section first Page of pdf *** ")
        else:
            print(f"Error :: 'processCharge' :'{processCharge}' is not matched with CHARGES Section first Page of pdf ")

        assert processCharge in firstPage, "processCharge is matched with CHARGES Section first Page of pdf"


        #Document Charges @1%
        docChargFloat = (loanAmountInt/100) * 1
        documentCharges = "₹" + str(docChargFloat) + "0"

        if documentCharges in firstPage:
            print(f" *** 'documentCharges' :'{documentCharges}' is matched and within CHARGES Section first Page of pdf *** ")
        else:
            print(f"Error :: 'documentCharges' :'{documentCharges}' is not matched and not within CHARGES Section first Page of pdf ")

        assert documentCharges in firstPage, "is matched and within CHARGES Section first Page of pdf"



        # 9% SGST is inclusive As specified by Government of India
        onlineConvenienceFees = 100
        sgstFloat = ((processChargeInt + docChargFloat + onlineConvenienceFees) / 100) * 9
        sgst = "₹" + str(round(sgstFloat,1))

        if sgst in firstPage:
            print(f" *** 'sgst' :'{sgst}' is matched with CHARGES Section first Page of pdf *** ")
        else:
            print(f"Error :: 'sgst' :'{sgst}' is not matched with CHARGES Section first Page of pdf ")

        assert sgst in firstPage, "is matched with CHARGES Section first Page of pdf"

        # 9% CGST is inclusive As specified by Government of India
        onlineConvenienceFees = 100
        cgstFloat = ((processChargeInt + docChargFloat + onlineConvenienceFees) / 100) * 9
        cgst = "₹" + str(round(cgstFloat,1))

        if cgst in firstPage:
            print(f" *** 'cgst' :'{cgst}' is matched with CHARGES Section first Page of pdf *** ")
        else:
            print(f"Error :: 'cgst' :'{cgst}' is not matched with CHARGES Section first Page of pdf ")

        assert cgst in firstPage, "is matched with CHARGES Section first Page of pdf"


        #Online convenience fees
        onlineConvenienceFeesString = "₹" + str(onlineConvenienceFees)
        if onlineConvenienceFeesString in firstPage:
            print(f" *** 'onlineConvenienceFeesString' :'{onlineConvenienceFeesString}' is inside CHARGES Section first Page of pdf *** ")
        else:
            print(f"Error :: 'onlineConvenienceFeesString' :'{onlineConvenienceFeesString}' is not inside CHARGES Section first Page of pdf ")

        assert onlineConvenienceFeesString in firstPage, "is inside CHARGES Section first Page of pdf"


        #Cheque / ECS / SI Return charges
        chequeBounceCharge = "₹ 500"
        if chequeBounceCharge in firstPage:
            print(f" *** 'chequeBounceCharge' :'{chequeBounceCharge}' is inside CHARGES Section first Page of pdf *** ")
        else:
            print(f"Error :: 'chequeBounceCharge' :'{chequeBounceCharge}' is not inside CHARGES Section first Page of pdf ")

        assert chequeBounceCharge in firstPage, "is inside CHARGES Section first Page of pdf"


        #Default Interest / Late Payment charges (per day)
        latePaymentChargePerDay = flotLIPD * 2
        latePaymentChargePerDayString = str(latePaymentChargePerDay) + "%"


        if latePaymentChargePerDayString in firstPage:
            print(f" *** 'latePaymentChargePerDayString' :'{latePaymentChargePerDayString}' is matched and is inside CHARGES Section first Page of pdf *** ")
        else:
            print(f"Error :: 'latePaymentChargePerDayString' :'{latePaymentChargePerDayString}' is not matched and not inside CHARGES Section first Page of pdf ")

        assert latePaymentChargePerDayString in firstPage, "is matched and within CHARGES Section first Page of pdf"


        # Default Interest / Late Payment charges (per annual)
        latePaymentChargePerAnnual = loanIntPerAnnum * 2
        latePaymentChargePerAnnualString = str(latePaymentChargePerAnnual) + "00%"

        if latePaymentChargePerAnnualString in firstPage:
            print(f" *** 'latePaymentChargePerAnnualString' :'{latePaymentChargePerAnnualString}' is matched with CHARGES Section first Page of pdf *** ")
        else:
            print(f"Error :: 'latePaymentChargePerAnnualString' :'{latePaymentChargePerAnnualString}' is not matched with CHARGES Section first Page of pdf ")

        assert latePaymentChargePerAnnualString in firstPage, "is matched with CHARGES Section first Page of pdf"


        #Stamp Duty & Other Statutoty Charges :
        # legalCollection = "300"
        stampChargeString1 = "300"
        if stampChargeString1 in firstPage:
            print(f" *** 'stampChargeString1' :'{stampChargeString1}' is matched with CHARGES Section first page of pdf *** ")
        else:
            print(f"Error :: 'stampChargeString1' :'{stampChargeString1}' is not matched with CHARGES Section first page of pdf ")

        assert stampChargeString1 in firstPage, "is matched with CHARGES Section first page of pdf"


        '''LETTER OF SANCTION TO THE BORROWER'''

        # Total amount to be paid
        totalCost = driver.find_element(By.XPATH,"//div[contains(@class,'font-weight-bold numbers mobile-text')]").text

        if totalCost in thirdPage:
            print(f" *** 'totalCost' :'{totalCost}' is matched with LETTER OF SANCTION TO THE BORROWER Section third page of pdf *** ")
        else:
            print(f"Error :: 'totalCost' :'{totalCost}' is not matched with LETTER OF SANCTION TO THE BORROWER Section third page of pdf ")

        assert totalCost in thirdPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section third page of pdf"


        #TOTAL PERIOD
        time.sleep(1)
        loanDurationInDays = loanDurInDays + " days"
        totalPeriod = loanDurationInDays
        if totalPeriod in thirdPage:
            print(f" *** 'totalPeriod' :'{totalPeriod}' is matched with LETTER OF SANCTION TO THE BORROWER Section third page of pdf *** ")
        else:
            print(f"Error :: 'totalPeriod' :'{totalPeriod}' is not matched with LETTER OF SANCTION TO THE BORROWER Section third page of pdf ")

        assert totalPeriod in thirdPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section third page of pdf"


        #COMMENCING FROM
        # LoanDisbursementDate = driver.find_element(By.XPATH,"//tr[contains(@class,'mat-row cdk-row loan-history-row bg-greywhite ng-star-inserted')]//td[6]//div").text
        LoanDisbursementDate = driver.find_element(By.XPATH,"(//div[@class='mobile-text fnt-size-12 ng-star-inserted'])[3]").text
        commencingFrom = LoanDisbursementDate.replace('/','-')
        time.sleep(1)
        if commencingFrom in thirdPage:
            print(f" *** 'commencingFrom' :'{commencingFrom}' is matched with LETTER OF SANCTION TO THE BORROWER Section third page of pdf *** ")
        else:
            print(f"Error :: 'commencingFrom' :'{commencingFrom}' is not matched with LETTER OF SANCTION TO THE BORROWER Section third page of pdf ")

        assert commencingFrom in thirdPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section third page of pdf"


        #DISBURSEMENT

        #STAMP CHARGES
        stampCharge = 300
        stampChargeString2 = "₹300.00/-"
        if stampChargeString2 in thirdPage:
            print(f" *** 'stampChargeString2' :'{stampChargeString2}' is matched with LETTER OF SANCTION TO THE BORROWER Section third page of pdf *** ")
        else:
            print(f"Error :: 'stampChargeString2' :'{stampChargeString2}' is not matched with LETTER OF SANCTION TO THE BORROWER Section third page of pdf ")

        assert stampChargeString2 in thirdPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section third page of pdf"


        # ONLINE CONVENIENCE CHARGES
        onlineConvCharge = 100
        onlineConvChargeString = "₹100"
        if onlineConvChargeString in thirdPage:
            print(f" *** 'onlineConvChargeString' :'{onlineConvChargeString}' is inside LETTER OF SANCTION TO THE BORROWER Section third page of pdf *** ")
        else:
            print(f"Error :: 'onlineConvChargeString' :'{onlineConvChargeString}' is not inside LETTER OF SANCTION TO THE BORROWER Section third page of pdf ")

        assert onlineConvChargeString in thirdPage, "is inside LETTER OF SANCTION TO THE BORROWER Section third page of pdf"


        #INSURANCE CHARGES
        insCharg = float(insurancePremAmount[1:])


        #DISBURSEMENT

        disburse = loanAmountInt - (processChargeInt + docChargFloat + stampCharge + onlineConvCharge + insCharg + sgstFloat + cgstFloat)
        disFloat = str(disburse)
        disbursement = "₹" + disFloat[0:2]+ "," + disFloat[2:3]
        if disbursement in thirdPage:
            print(f" *** 'disbursement' :'{disbursement}' is matched with LETTER OF SANCTION TO THE BORROWER Section third page of pdf *** ")
        else:
            print(f"Error :: 'disbursement' :'{disbursement}' is not matched with LETTER OF SANCTION TO THE BORROWER Section third page of pdf ")

        assert disbursement in thirdPage, "is matched with LETTER OF SANCTION TO THE BORROWER Section third page of pdf"


        '''SECURITY DOCUMENTS'''

        #Sanction Days
        sanctionDays = "10 days"
        if sanctionDays in fourthPage:
            print(f" *** 'sanctionDays' :'{sanctionDays}' is matched with SECURITY DOCUMENTS fourth page of pdf *** ")
        else:
            print(f"Error :: 'sanctionDays' :'{sanctionDays}' is not matched with SECURITY DOCUMENTS fourth page of pdf ")

        assert sanctionDays in fourthPage, "is matched with SECURITY DOCUMENTS fourth page of pdf"


        #Penal interest per day

        penalInterestPerDay = latePaymentChargePerDayString
        if penalInterestPerDay in fourthPage:
            print(f" *** 'penalInterestPerDay' :'{penalInterestPerDay}' is matched with SECURITY DOCUMENTS fourth Page of pdf *** ")
        else:
            print(f"Error :: 'penalInterestPerDay' :'{penalInterestPerDay}' is not matched with SECURITY DOCUMENTS fourth Page of pdf ")

        assert penalInterestPerDay in fourthPage, "penalInterestPerDay is matched with SECURITY DOCUMENTS fourth Page of pdf"

        # Penal interest per annum

        penalInterestPerAnnum = latePaymentChargePerAnnualString
        if penalInterestPerAnnum in fourthPage:
            print(f" *** 'penalInterestPerAnnum' :'{penalInterestPerAnnum}' is matched with SECURITY DOCUMENTS fourth Page of pdf *** ")
        else:
            print(f"Error :: 'penalInterestPerAnnum' :'{penalInterestPerAnnum}' is not matched with SECURITY DOCUMENTS fourth Page of pdf ")

        assert penalInterestPerAnnum in fourthPage, "penalInterestPerAnnum is matched with SECURITY DOCUMENTS fourth Page of pdf"


        #Name of Borrower in security document
        try:
            if profileName in fourthPage:
                print(f" *** 'profileName':'{profileName}' is matched with security document in fourth Page of pdf *** ")
            else:
                print(f"Exception :: 'profileName':'{profileName}' is not matched with security document in fourth Page of pdf ")

            assert profileName in fourthPage, "profileName is matched with security document in fourth Page of pdf"

        except:
            if 'Name of Borrower' in firstPage:
                index1 = firstPage.index('Name of Borrower')
                index2 = firstPage.index('NBFC NameChinmay Finlease')
                text = firstPage[index1 + 16:index2]
                print(f"Name by pdf module :: {text}")




        '''LOAN AGREEMENT'''
        #Name of Borrower in loan agreement

        if profileName in sixthPage:
            print(f" *** 'profileName':'{profileName}' is matched with LOAN AGREEMENT sixth Page of pdf *** ")
        else:
            print(f"Exception :: 'profileName':'{profileName}' is not matched with LOAN AGREEMENT sixth Page of pdf ")

        assert profileName in sixthPage, "profileName is matched with LOAN AGREEMENT sixth Page of pdf"


        # Email
        # driver.find_element(By.XPATH,"(//button[@class='details-view-btn ml-2 ng-star-inserted'][normalize-space()='View'])[2]").click()
        # email = driver.find_element(By.XPATH,"//div[contains(text(),'umesh31849@gmail.com')]").text
        # time.sleep(2)
        emailS = driver.find_element(By.XPATH,"/html[1]/body[1]/app-root[1]/app-layout[1]/div[3]/mat-drawer-container[1]/mat-drawer-content[1]/div[1]/app-customer-list[1]/div[1]/div[2]/div[2]/app-customer-basic-details[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]").text
        time.sleep(2)
        eindex = emailS.index("View")
        email= emailS[:eindex-1]
        # print(n)

        if email in sixthPage:
            print(f" *** 'email' :'{email}' is matched with LOAN AGREEMENT sixth Page of pdf *** ")
        else:
            print(f"Exception :: 'email' :'{email}' is not matched with LOAN AGREEMENT sixth Page of pdf ")

        assert email in sixthPage, "email is matched with LOAN AGREEMENT sixth Page of pdf"


        # PAN number
        pan = driver.find_element(By.XPATH,"//div[contains(@class,'basic-details d-flex flex-row basic-info-card align-items-center justify-content-between mt-2')][2]//div[2]").text
        time.sleep(1)
        if pan in sixthPage:
            print(f" *** 'pan' :'{pan}' is matched with LOAN AGREEMENT sixth Page of pdf *** ")
        else:
            print(f"Error :: 'pan' :'{pan}' is not matched with LOAN AGREEMENT sixth Page of pdf ")

        assert pan in sixthPage, "pan is matched with LOAN AGREEMENT sixth Page of pdf"


        # loan amount
        lA = approvedAmount
        loanAmountstr = lA.replace("/-","")
        if loanAmountstr in sixthPage:
            print(f" *** 'loanAmountstr' :'{loanAmountstr}' is matched with LOAN AGREEMENT sixth Page of pdf *** ")
        else:
            print(f"Error :: 'loanAmountstr' :'{loanAmountstr}' is not matched with LOAN AGREEMENT sixth Page of pdf ")

        assert loanAmountstr in sixthPage, "loanAmountstr is matched with LOAN AGREEMENT sixth Page of pdf"

        # loan period
        if loanDurationInDays in sixthPage:
            print(f" *** 'loanDurationInDays' :'{loanDurationInDays}' is matched with LOAN AGREEMENT sixth Page of pdf *** ")
        else:
            print(f"Error :: 'loanDurationInDays' :'{loanDurationInDays}' is not matched with LOAN AGREEMENT sixth Page of pdf ")

        assert loanDurationInDays in sixthPage, "loanDurationInDays is matched with LOAN AGREEMENT sixth Page of pdf"


        # loan interest
        #per day
        if loanInterestPerDay in sixthPage:
            print(f" *** 'loanInterestPerDay' :'{loanInterestPerDay}' is matched with LOAN AGREEMENT sixth Page of pdf *** ")
        else:
            print(f"Error :: 'loanInterestPerDay' :'{loanInterestPerDay}' is not matched with LOAN AGREEMENT sixth Page of pdf ")

        assert loanInterestPerDay in sixthPage, "loanInterestPerDay is matched with LOAN AGREEMENT sixth Page of pdf"

        #per annum
        if loanIntPerAnnumStr in sixthPage:
            print(f" *** 'loanIntPerAnnumStr' :'{loanIntPerAnnumStr}' is matched with LOAN AGREEMENT sixth Page of pdf *** ")
        else:
            print(f"Error :: 'loanIntPerAnnumStr' :'{loanIntPerAnnumStr}' is not matched with LOAN AGREEMENT sixth Page of pdf ")

        assert loanIntPerAnnumStr in sixthPage, "loanIntPerAnnumStr is matched with LOAN AGREEMENT sixth Page of pdf"


        # penalty interest
        #per day
        if latePaymentChargePerDayString in sixthPage:
            print(f" *** 'latePaymentChargePerDayString' :'{latePaymentChargePerDayString}' is matched with LOAN AGREEMENT sixth Page of pdf *** ")
        else:
            print(f"Error :: 'latePaymentChargePerDayString' :'{latePaymentChargePerDayString}' is not matched with LOAN AGREEMENT sixth Page of pdf ")

        assert latePaymentChargePerDayString in sixthPage, "latePaymentChargePerDayString is matched with LOAN AGREEMENT sixth Page of pdf"

        #per annum

        if latePaymentChargePerAnnualString in sixthPage:
            print(f" *** 'latePaymentChargePerAnnualString' :'{latePaymentChargePerAnnualString}' is matched with LOAN AGREEMENT sixth Page of pdf *** ")
        else:
            print(f"Error :: 'latePaymentChargePerAnnualString' :'{latePaymentChargePerAnnualString}' is not matched with LOAN AGREEMENT sixth Page of pdf ")

        assert latePaymentChargePerAnnualString in sixthPage, "latePaymentChargePerAnnualString is matched with LOAN AGREEMENT sixth Page of pdf"


        '''Borrower Name in ninth page'''
        try:
            if profileName in ninthPage:
                print(f" *** 'profileName':'{profileName}' is matched with witness in ninth Page of pdf *** ")
            else:
                print(f"Exception :: 'profileName':'{profileName}' is not matched with witness in ninth Page of pdf ")

            assert profileName in ninthPage, "profileName is matched with witness in ninth Page of pdf"
        except:
            if 'Name of Borrower' in firstPage:
                index1 = firstPage.index('Name of Borrower')
                index2 = firstPage.index('NBFC NameChinmay Finlease')
                text = firstPage[index1 + 16:index2]
                print(f"Name by pdf module :: {text}")



