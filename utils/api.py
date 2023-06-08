from utils.http_methods import Http_methods

"""Google API testing methods"""

base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"


class Google_maps_api():

    """New place creating"""
    @staticmethod
    def create_new_place():

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json"
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_create_new_place)
        print(result_post.text)

        return result_post

    """Place information"""
    @staticmethod
    def get_place_information(place_id):
        """Existing place information"""

        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)

        return result_get

    @staticmethod
    def put_new_place(place_id):
        """PUT new address for existing place"""

        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        print(put_url)
        result_put = Http_methods.put(put_url, json_for_update_new_location)
        print(result_put.text)

        return result_put

    @staticmethod
    def delete_place(place_id):
        """Delete existing location"""

        del_resource = "/maps/api/place/delete/json"
        del_url = base_url + del_resource + key
        print(del_url)
        json_for_del_new_location = {
            "place_id": place_id
        }
        result_del = Http_methods.delete(del_url, json_for_del_new_location)
        # print(result_del.status_code)
        print(result_del.text)

        return result_del

