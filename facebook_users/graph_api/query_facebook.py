import os
from facebook_users.graph_api.facebook_query_factory import FacebookQuery, QueryType

def authenticate_token(token):
    facebook_query = FacebookQuery(QueryType.LOG_IN_WITH_TOKEN, input_token = token,
    access_token = os.environ["SOCIAL_TODO_APP_ID"] + "|" + os.environ["SOCIAL_TODO_APP_SECRET"])
    return facebook_query.get_json()


class FacebookFriendFinder(object):
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token
        self.friends_list = set()
        self.finished = False
        self.__get_friends_list()
        assert(self.finished == True)

    def __get_friends_list(self,after = None):
        if after is None:
            facebook_query = FacebookQuery(QueryType.GET_FRIENDS_LIST, user_id = self.user_id, input_token = self.token,
                access_token = os.environ["SOCIAL_TODO_APP_ID"] + "|" + os.environ["SOCIAL_TODO_APP_SECRET"])
        else:
            facebook_query = FacebookQuery(QueryType.GET_FRIENDS_LIST, user_id = self.user_id, input_token = self.token,
                access_token = os.environ["SOCIAL_TODO_APP_ID"] + "|" + os.environ["SOCIAL_TODO_APP_SECRET"],
                after = after)
        self.__parse_graph_response(facebook_query.get_json())

    def __parse_graph_response(self,graph_response):
        if(len(graph_response['data']) != 0):
            self.__add_friend_page_to_list(graph_response["data"])
            self.__get_friends_list(after=graph_response["paging"]["cursors"]["after"])
        else:
            self.finished = True

    def __add_friend_page_to_list(self,data):
        for friend in data:
            self.friends_list.add(friend["id"])

    def get_friends(self):
        if self.finished:
            return self.friends_list
        else:
            return None