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
ninthPage = reader.pages[8].extract_text()

print(firstPage)

umeshsai1995@gmail.com,
umeshsai1995@gmail.com

# if 'Accepted' in fourthPage:
#     index1 = fourthPage.index('Accepted')
#     index2 = fourthPage.index('( Name of the borrower )')
#     text = fourthPage[index1+251:index2]
#     print(f"Name by pdf module :: {text}")

