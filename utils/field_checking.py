import json

from requests import Response


class FieldChecking():
    """Mandatory fields checking in response body"""

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print('All fields are')