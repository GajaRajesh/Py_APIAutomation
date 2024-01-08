class APIConstants:
    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    def url_update_booking(self,booking_id):
        return "https://restful-booker.herokuapp.com/booking/"+str(booking_id)

