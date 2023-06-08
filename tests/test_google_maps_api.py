from requests import Response
from utils.api import Google_maps_api

"""CRUD new location"""
class Test_create_place():

    def test_create_new_place(self):
        print(">> POST method")
        result_post: Response = Google_maps_api.create_new_place()
        place_id = result_post.json().get('place_id')
        print(place_id)

        print(">> GET method")
        result_get: Response = Google_maps_api.get_place_information(place_id=place_id)