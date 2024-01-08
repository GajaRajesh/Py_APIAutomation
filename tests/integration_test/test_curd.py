from Src.constants import api_constants
import requests
def test_demo1():
    response=requests.post(api_constants.APIConstants.base_url())
    print(response.status_code)