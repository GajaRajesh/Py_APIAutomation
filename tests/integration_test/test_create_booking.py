from Src.helpers.api_requests_wrapper import ApiRequests
from Src.constants.api_constants import APIConstants
from Src.helpers.utils import CommonHeaders
from Src.helpers.Payload_Manager import PayloadManager
from Src.helpers.Common_Verification import CommonVerification


class TestCreateBooking:
    def test_create_booking_tc1(self):
        response= ApiRequests().post_request(
            url=APIConstants.url_create_booking(),
            auth=None,headers=CommonHeaders().coomon_headers_json(),
        payload=PayloadManager().payload_create_booking(),in_json=False
        )
        print(response.json())
        CommonVerification().verify_http_status_code(response,200)
        CommonVerification().verify_json_key_for_not_null(response.json()["bookingid"])
        bookingid=response.json()["bookingid"]
        print(bookingid)
        return bookingid
    def test_create_booking_tc2(self):
        response=ApiRequests().post_request(
            url=APIConstants().url_create_booking(),auth=None,headers=CommonHeaders().coomon_headers_json(),
            payload={},in_json=False
        )
        CommonVerification().verify_http_status_code(response,500)







