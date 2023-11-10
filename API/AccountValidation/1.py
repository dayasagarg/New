import pytest
import requests
from requests.auth import HTTPBasicAuth
import json
import time
from datetime import datetime

'''# WALLET SETTLEMENT TOTAL'''
walletSettlAPIResp = requests.get(
    "https://lendittfinserve.com/prod/admin/tally/getWalletSettlementDetails?startDate=2023-10-08T10%3A00%3A00.000Z&endDate=2023-10-08T10%3A00%3A00.000Z")  # current date   Note: On holiday, data will not available.

'''# RAZORPAY-1'''
razPay1 = requests.get("https://api.razorpay.com/v1/settlements",
                       params={"from": 1695081600, "to": 1695168000},
                       auth=HTTPBasicAuth("rzp_live_b6RhLeN8cATRGq", "mLimxgzWR1vuOaamr5IvU8MC"),
                       )  # from date = previous date, #to date = current date (in unix format)

print(razPay1.json())

