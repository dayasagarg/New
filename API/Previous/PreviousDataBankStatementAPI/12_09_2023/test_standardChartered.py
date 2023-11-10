import requests
import pytest


class TestPost:

    def test_postRBcS1(self):
        url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\12-09-2023\sc1.pdf"
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


    def test_postRBcS2(self):
        url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\12-09-2023\sc2.pdf"
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


    def test_postRBcS3(self):
        url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\12-09-2023\sc3.pdf"
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
        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\12-09-2023\sc4.pdf"
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


    def test_postRBcS5(self):
        url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\12-09-2023\sc5.pdf"
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


