from Src.helpers.api_requests_wrapper import ApiRequests
from Src.constants.api_constants import APIConstants
from Src.helpers.utils import CommonHeaders
from Src.helpers.Payload_Manager import PayloadManager
from Src.helpers.Common_Verification import CommonVerification
import pytest
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import os


class TestCreateBooking:
    def load_schema(self,file_path):
        with open(file_path) as file:
            return json.load(file)

    @pytest.mark.positive
    def test_create_booking_jsonschema(self):
        response = ApiRequests().post_request(
            url=APIConstants.url_create_booking(),
            auth=None, headers=CommonHeaders().coomon_headers_json(),
            payload=PayloadManager().payload_create_booking(), in_json=False
        )
        json_response = response.json()
        file_path=os.getcwd()+"\\schema.json"
        schema= self.load_schema(file_path)
        print(json_response)
        try:
            validate(instance=json_response, schema=schema)
            print("sucessfully completed")
        except ValidationError as e:
            print(e)

