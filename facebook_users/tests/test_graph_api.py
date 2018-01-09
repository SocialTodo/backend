from django.test import TestCase
from facebook_users import authentication
from django.core.exceptions import PermissionDenied


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
