from django.test import TestCase
from facebook_users import authentication
from facebook_users.graph_api.query_facebook import FacebookFriendFinder
from facebook_users.graph_api import query_facebook
from django.core.exceptions import PermissionDenied
from facebook_users.graph_api.facebook_query_factory import QueryType, QueryTypeNotFound
from facebook_users.graph_api import facebook_query_factory


class UserLogin(TestCase):
    def setUp(self):
        authentication.authenticate_token = mock_authenticate_token

    def test_valid_user(self):
        response = authentication.FacebookBackend.query_facebook(self, "1234")
        self.assertTrue(response == "123456")

    def test_invalid_user(self):
        with self.assertRaises(PermissionDenied):
            authentication.FacebookBackend.query_facebook(self, "12345")


def mock_authenticate_token(token):
    if (token == "1234"):
        return {
            'data': {
                'app_id': '293904984347643',
                'type': 'USER',
                'application': 'Social Todo List',
                'expires_at': 1520647284,
                'is_valid': True,
                'issued_at': 1515463284,
                'metadata': {
                    'auth_type': 'rerequest',
                    'sso': 'iphone-safari'},
                'scopes': [
                    'user_friends',
                    'email',
                    'public_profile'],
                'user_id': '123456'}}
    else:
        return {'data': {'error':
                         {'code': 190,
                          'message': 'Invalid OAuth access token.'},
                         'is_valid': False, 'scopes': []}}


class LoadFriends(TestCase):
    def setUp(self):
        query_facebook.LIST_POSITION = 0
        query_facebook.FacebookQuery = MockFacebookQuery

    def test_friends_added(self):
        facebook_friend_finder = FacebookFriendFinder(
            "2317825702628370",
            "dakfljdskafjdklsajfkdjadslkfjslkafdksjalksjfksajflksdjsakfj")
        expected = {6316816636194673,
                2467825702628370,
                1117789108273389,
                2418890580099085,
                9163667750244648,
                2999009655073479,
                9038707755843264,
                6991266520965726,
                2749147975847501,
                3707558171063215,
                4588976795742594}
        self.assertTrue(facebook_friend_finder.get_friends() == expected)


class MockFacebookQuery(object):
    def __init__(self, query_type, **kwargs):
        self.query_type = query_type
        # These names were randomly generated, I don't have enough friends to test
        # this function for real
        self.test_friends = [
            {"name": "Alondra Krause", "id": 6316816636194673}, {"name": "Eliana Cordova", "id": 2467825702628370}, {"name": "Tori Howell", "id": 1117789108273389}, 
            {"name": "Rey Dickson", "id": 2418890580099085}, {"name": "Phoenix Andrews", "id": 9163667750244648}, {"name": "Talon Farmer", "id": 2999009655073479}, 
            {"name": "Carolina Cortez", "id": 9038707755843264}, {"name": "Penelope Velazquez", "id": 6991266520965726}, {"name": "Giancarlo Manning", "id": 2749147975847501}, 
            {"name": "Camron Oliver", "id": 3707558171063215}, {"name": "Moriah Cross", "id": 4588976795742594}
            ]
        self.list_position = query_facebook.LIST_POSITION


    def get_json(self):
        if self.query_type == QueryType.GET_FRIENDS_LIST:
            if self.list_position >= len(self.test_friends):
                return {
                    "data": [],
                    "paging": {
                        "cursors": {
                            "before": "kdlajfkdslajfkdslajfdksafjl",
                            "after": "kdafjlsdklfjdkslafjkdjaflfdj"
                            }
                        }
                    }
            else:
                response = {
                    "data": self.test_friends[self.list_position:min(len(self.test_friends),self.list_position + 3)],
                    "paging": {
                        "cursors": {
                            "before": "kdlajfkdslajfkdslajfdksafjl",
                            "after": "kdafjlsdklfjdkslafjkdjaflfdj"
                            }
                        }
                    }
                query_facebook.LIST_POSITION = self.list_position + 3
                return response
