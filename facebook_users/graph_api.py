import requests
import os


def authenticate_token(token):
    return requests.get(
        "https://graph.facebook.com/debug_token",
        params={
            "input_token": token,
            "access_token": os.environ["SOCIAL_TODO_APP_ID"] +
            "|" +
            os.environ["SOCIAL_TODO_APP_SECRET"]}).json()


class FacebookFriendFinder(object):
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token

    def __get_friends(self):
        return requests.get(
            "https://graph.facebook.com/{}/friends".format(self.user_id),
            params={
                "input_token": self.token,
                "access_token": os.environ["SOCIAL_TODO_APP_ID"] +
                "|" +
                os.environ["SOCIAL_TODO_APP_SECRET"]}).json()
