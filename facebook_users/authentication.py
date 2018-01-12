from django.contrib.auth import get_user_model
User = get_user_model()
import json
from django.core.exceptions import PermissionDenied
from django.conf import settings
from facebook_users.graph_api.query_facebook import authenticate_token, FacebookFriendFinder
import logging
logging.basicConfig(level=logging.DEBUG)


class CachedFacebookBackend(object):
    """Return a user if the user has logged in before
    with their current facebook token (i.e. it hasn't expired
    since the last login)
    """

    def authenticate(self, request, token=None):
        try:
            user_provided_token, user_provided_id = self.parse_request(request)
            user = self.get_user(user_provided_id)
            if user is not None and user.facebook_token == token:
                logging.debug(
                    "User {} successfully logged in via CachedFacebookBackend!".format(user_provided_id))
                return user
            logging.debug(
                "User {} does have an account, but the provided token did not match the cached token!".format(user_provided_id))
            return None
        except User.DoesNotExist:
            logging.debug(
                "User {} does not yet have an account!".format(user_provided_id))
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def parse_request(self, request):
        response_body = json.loads(request.body)
        return (response_body["Token"], response_body["UserID"])


class FacebookBackend(object):
    """Return a user if the user has not logged in
    before or their facebook token has expired
    """

    def authenticate(self, request, token=None):
        try:
            facebook_response = self.query_facebook(token)
            user_provided_token, user_provided_id = CachedFacebookBackend.parse_request(
                self, request)
            if facebook_response == user_provided_id:
                user, created = User.objects.get_or_create(
                    facebook_user_id=user_provided_id)
                if created:
                    user.set_unusable_password()
                    user.facebook_token = user_provided_token
                elif not user.facebook_token == user_provided_token:
                    user.facebook_token == user_provided_token
                FacebookFriendFinder(user_provided_id,user_provided_token)
                return user
        except PermissionDenied:
            logging.debug(
                "User {} failed to authenticate with Facebook! Could the token be expired?".format(user_provided_id))
            return None
        return None

    def get_user(self, user_id):
        CachedFacebookBackend.get_user(user_id)

    def query_facebook(self, token):
        fb_graph_dictionary = authenticate_token(token)
        request_successful = fb_graph_dictionary["data"]["is_valid"]
        logging.debug(
            "Facebook graph request returned {}".format(request_successful))
        if not request_successful:
            raise PermissionDenied
        return fb_graph_dictionary["data"]["user_id"]
