import requests


url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
pdfFile = "C:\\Users\\lendi\\Downloads\\netBanking_name change (1).pdf"
files = {"pdfFile": open(pdfFile, "rb")}
headers = {

    "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
}
data = {"bankCode": "ICICI"}

response = requests.post(url, files=files, headers=headers, data=data)

print(response.json())
print("status_code::",response.status_code)
print("valid::",response.json()['valid'])
