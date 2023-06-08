import json

import self as self
from requests import Response
from utils.api import Google_maps_api
from utils.checking import Checking
from utils.field_checking import FieldChecking

"""CRUD new location"""
class Test_create_place:

    place_id: str = ''

    def test_create_new_place(self):
        print(">> POST method")
        result_post: Response = Google_maps_api.create_new_place()
        self.place_id = result_post.json().get('place_id')
        print(self.place_id)
        # Checking.check_status_code(result_post, 200)
        # FieldChecking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        # token = json.loads(result_post.text)
        # print(list(token))

        # print(">> GET POST")
        # result_get: Response = Google_maps_api.get_place_information(place_id=place_id)
        #
        # print(">> PUT method")
        # result_put: Response = Google_maps_api.put_new_place(place_id=place_id)
        # FieldChecking.check_json_token(response=result_put, expected_value=['msg'])

        # print(">> GET PUT")
        # result_get: Response = Google_maps_api.get_place_information(place_id=place_id)
        #
        # print(">> DELETE method")
        # result_delete: Response = Google_maps_api.delete_place(place_id=place_id)
        # Checking.check_status_code(result_delete, 200)
        #
        # print(">> GET after DELETE")
        # result_get: Response = Google_maps_api.get_place_information(place_id=place_id)
        # Checking.check_status_code(result_get, 404)

    def test_get_existing_place(self):
        print(">> GET POST")
        result_get: Response = Google_maps_api.get_place_information(self.place_id)