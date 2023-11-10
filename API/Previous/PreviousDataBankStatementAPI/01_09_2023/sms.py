from __future__ import print_function

import requests
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint


#
# configuration = sib_api_v3_sdk.Configuration()
# configuration.api_key['api-key'] = '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'
#
# api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
# subject = "My Subject2"
# html_content = "<html><body><h1>This is message 2 </h1></body></html>"
# sender = {"name":"dsg","email":"dayasagar.ghodake@lenditt.com"}
# to = [{"email":"dayasagar.ghodake@lenditt.com","name":"dsg2"}]
# cc = [{"email":"example2@example2.com","name":"Janice Doe"}]
# bcc = [{"name":"John Doe","email":"example@example.com"}]
# reply_to = {"email":"replyto@domain.com","name":"John Doe"}
# headers = {"Some-Custom-Name":"unique-id-1234"}
# params = {"parameter":"My param value","subject":"New Subject"}
# send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, bcc=bcc, cc=cc, reply_to=reply_to, headers=headers, html_content=html_content, sender=sender, subject=subject)
#
# try:
#     api_response = api_instance.send_transac_email(send_smtp_email)
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)







headers = {

    "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
}

bankCode = "AXIS"
pdfFile = "C:\\Users\\lendi\\Downloads\\netBanking_name change (1).pdf"

url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL

files = {"pdfFile": open(pdfFile, "rb")}

data = {"bankCode": "STANDARD_CHARTERED"}

response = requests.post(url, files=files, headers=headers, data=data)



# {'valid': False, 'message': 'Please download valid statement from the bank site', 'errorCode': 101}
# print('valid::', response.json()['valid'])
# print('message::', response.json()['message'])
# print('errorCode::', response.json()['errorCode'])


info = response.json()
# print(info)

l = []

for data in info:
    value = data['value']
    if value == "False":
        l.append(value)



print(l)

print