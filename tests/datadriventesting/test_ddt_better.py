import openpyxl
import pytest
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
        print(credentials)
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
@pytest.mark.parametrize("user_cred",
                         read_credentials_from_excel(
                             "\\Users\\rajes\\PycharmProjects\\Py1xAPIAutomation\\tests\\datadriventesting\\Login_data.xlsx"))
def test_post_create_token(user_cred):
        username=user_cred["username"]
        password=user_cred["password"]
        print(username,password)
        response=make_request_auth(username,password)
        print(response)
        assert response.status_code==200,"not 200"
