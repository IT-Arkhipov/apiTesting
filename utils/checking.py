from requests import Response

"""Results checking methods"""
class Checking():

    """Status code checking"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        # try:
        #     assert status_code == response.status_code
        # except AssertionError:
        #     print('-- Wrong status code! -- ' + str(response.status_code))
        # else:
        #     print('Status code is OK: ' + str(response.status_code))
        # finally:
        #     pass
