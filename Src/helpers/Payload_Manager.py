class PayloadManager:
    def payload_create_booking(self):
        response = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        return response
    def payload_create_booking_update(self):
        response={
            "firstname": "Rajesh",
            "lastname": "wise",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        return response

    def payload_create_token(self):
        response = {
            "username": "admin",
            "password": "password123"
        }
        return response
