import requests


class TestPost:

    def test_postRBcS1(self):
        url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
        pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\bank statements\JUN TO SEPT 2023.pdf"
        files = {"pdfFile": open(pdfFile, "rb")}
        headers = {

            "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
            "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
        }

        data = {"bankCode": "CANARA"}

        response = requests.post(url, files=files, headers=headers, data=data)
        print('statusCode::', response.status_code)
        print('valid::', response.json()['valid'])

        # print(response.json())

        assert response.status_code == 201
        assert response.json()['valid'] == True


    # def test_postRBcS2(self):
    #     url = "http://144.24.112.239/bankingpro/statement/extractData"  # API URL
    #     pdfFile = r"C:\Users\lendi\OneDrive\Desktop\Daily Task\API\Bank Statement API\14-09-2023\Bank Statement\HDFC_524502.pdf"
    #     files = {"pdfFile": open(pdfFile, "rb")}
    #     headers = {
    #
    #         "secretKey": "U2FsdGVkX1+HiPbHmuY6O1hS+QdwL4BiPCxFz3heNro=",
    #         "appId": "e2caf6fe-beae-4c4d-bda8-8b489a24538c"
    #     }
    #
    #     data = {"bankCode": "HDFC"}
    #
    #     response = requests.post(url, files=files, headers=headers, data=data)
    #     print('statusCode::', response.status_code)
    #     print('valid::', response.json()['valid'])
    #
    #     # print(response.json())
    #
    #     assert response.status_code == 201
    #     assert response.json()['valid'] == True
    #
    #

