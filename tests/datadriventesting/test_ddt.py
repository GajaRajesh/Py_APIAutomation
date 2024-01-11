import openpyxl
import requests
from Src.constants.api_constants import APIConstants
from Src.helpers.api_requests_wrapper import ApiRequests
from Src.helpers.utils import CommonHeaders


def read_credentials_from_excel(file_path):
    credentials=[]
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2,values_only=True):
        username,password=row
        credentials.append({"username":username,
                            "password":password})
        #print(credentials)
    return credentials

def make_request_auth(username,password):
    payload={
        "username":username,
        "password":password
    }
    response=ApiRequests().post_request(url=APIConstants.url_create_token(),
                           headers=CommonHeaders().coomon_headers_json(),auth=None,
                           payload=payload,in_json=False)
    return response

def test_post_create_token():
    file_path="\\Users\\rajes\\PycharmProjects\\Py1xAPIAutomation\\tests\\datadriventesting\\Login_data.xlsx"
    credentials=read_credentials_from_excel(file_path)
    for user_cred in credentials:
        username=user_cred["username"]
        password=user_cred["password"]
        print(username,password)
        response=make_request_auth(username,password)
        print(response.json())
        #token=response.json()["token"]
        assert response.status_code==200,"not 200"
