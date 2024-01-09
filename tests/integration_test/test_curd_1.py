from requests.auth import HTTPBasicAuth

from Src.constants.api_constants import APIConstants
from Src.helpers.Common_Verification import CommonVerification
from Src.helpers.api_requests_wrapper import ApiRequests
from Src.helpers.utils import CommonHeaders
from Src.helpers.Payload_Manager import PayloadManager
import pytest

class TestCreateBooking:
    @pytest.fixture
    def create_token(self):
        response= ApiRequests().post_request(
            url=APIConstants.url_create_token(), auth=None,headers = CommonHeaders().coomon_headers_json(),
            payload = PayloadManager().payload_create_token(),in_json = False
        )
        token=response.json()["token"]
        return token

    @pytest.fixture
    def create_booking_tc1(self):
        response = ApiRequests().post_request(
            url=APIConstants.url_create_booking(),
            auth=None, headers=CommonHeaders().coomon_headers_json(),
            payload=PayloadManager().payload_create_booking(), in_json=False
        )
        print(response.json())
        CommonVerification().verify_http_status_code(response, 200)
        CommonVerification().verify_json_key_for_not_null(response.json()["bookingid"])
        bookingid = response.json()["bookingid"]
        print(bookingid)
        return bookingid

    def test_update_booking(self,create_token,create_booking_tc1):
        bookingid=create_booking_tc1
        URL=APIConstants().url_update_booking(bookingid)
        username = "admin"
        password = "password123"
        response=ApiRequests().put_request(
            url=URL,auth=HTTPBasicAuth(username,password),
            headers=CommonHeaders().coomon_headers_json(),
            payload=PayloadManager().payload_create_booking_update(),in_json=False)
