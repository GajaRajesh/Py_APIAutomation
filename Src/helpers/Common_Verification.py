class CommonVerification:

    def verify_http_status_code(self, response_data, expect_code):
        assert response_data.status_code == expect_code, "Expected code" + str(expect_code)

    def verify_json_key_for_not_null(self, key):
        assert key is not None, "the key is not none"
