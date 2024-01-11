from faker import Faker
from dotenv import load_dotenv
import os
import requests
from Src.helpers.utils import *
import json


def test_sample():
    load_dotenv()
    faker = Faker()
    json_payload = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=10, max=100),
        "depositpaid": faker.boolean(),
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": faker.random_element(elements=("Breakfast", "Lunch", "Dinner"))
    }
    response = requests.post(url="https://restful-booker.herokuapp.com/booking",
                             headers=CommonHeaders().coomon_headers_json(),
                             data=json.dumps(json_payload))
    print(response.json())

    username = os.getenv("NAME")
    password = os.getenv("PASSWORD")
    print(username, password)
