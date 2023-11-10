import requests
import pytest


class TestPost:

    def test_postWBcS1(self):
        url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\bank statements\netBanking_name change (1).pdf"
        files = {"pdfFile": open(pdfFile, "rb")}
        headers = {

            "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
            "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
        }

        data = {"bankCode": "STANDARD_CHARTERED"}

        response = requests.post(url, files=files, headers=headers, data=data)
        print('valid::',response.json()['valid'])
        print('message::', response.json()['message'])
        print('errorCode::', response.json()['errorCode'])
        # print('valid::', response.json())
        assert response.json()['valid'] == False
        assert response.json()['message'] == 'Please download valid statement from the bank site'
        assert response.json()['errorCode'] == 101


    def test_postWBcS2(self):
        url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\bank statements\netBanking_name change (1).pdf"
        files = {"pdfFile": open(pdfFile, "rb")}
        headers = {

            "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
            "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
        }

        data = {"bankCode": "SBI"}

        response = requests.post(url, files=files, headers=headers, data=data)
        print('valid::', response.json()['valid'])
        print('message::', response.json()['message'])
        print('errorCode::', response.json()['errorCode'])
        # print('valid::', response.json())
        assert response.json()['valid'] == False
        assert response.json()['message'] == 'Please download valid statement from the bank site'
        assert response.json()['errorCode'] == 101


    def test_postRBcS3(self):
        url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\bank statements\Standard Chartered.pdf"
        files = {"pdfFile": open(pdfFile, "rb")}
        headers = {

            "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
            "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
        }

        data = {"bankCode": "STANDARD_CHARTERED"}

        response = requests.post(url, files=files, headers=headers, data=data)
        print('statusCode::', response.status_code)
        print('valid::', response.json()['valid'])

        # print(response.json())

        assert response.status_code == 201
        assert response.json()['valid'] == True



    def test_postRBcS4(self):
        url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\bank statements\HDFC Statement.pdf"
        files = {"pdfFile": open(pdfFile, "rb")}
        headers = {

            "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
            "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
        }

        data = {"bankCode": "HDFC"}

        response = requests.post(url, files=files, headers=headers, data=data)
        print('statusCode::', response.status_code)
        print('valid::', response.json()['valid'])

        # print(response.json())

        assert response.status_code == 201
        assert response.json()['valid'] == True



    def test_postRBcS5(self):
        url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\bank statements\SBI Statement.pdf"
        files = {"pdfFile": open(pdfFile, "rb")}
        headers = {

            "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
            "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
        }

        data = {"bankCode": "SBI"}

        response = requests.post(url, files=files, headers=headers, data=data)
        print('statusCode::', response.status_code)
        print('valid::', response.json()['valid'])

        # print(response.json())

        assert response.status_code == 201
        assert response.json()['valid'] == True



