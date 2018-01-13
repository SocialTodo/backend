import requests
import os
import json
from enum import Enum

class QueryType(Enum):
  LOG_IN_WITH_TOKEN = 0
  GET_FRIENDS_LIST = 1
  GET_USER_INFO = 2

class FacebookQuery(object):
  def __init__(self, query_type, **kwargs):
    if query_type == QueryType.LOG_IN_WITH_TOKEN:
      self.request = {"url":"https://graph.facebook.com/debug_token","parameters":kwargs}
    elif query_type == QueryType.GET_FRIENDS_LIST:
      url = "https://graph.facebook.com/{}/friends".format(kwargs["user_id"])
      del kwargs["user_id"]
      self.request = {"url":url, "parameters":kwargs}
    elif query_type == QueryType.GET_USER_INFO:
      url = "https://graph.facebook.com/{}".format(kwargs["user_id"])
      del kwargs["user_id"]
      self.request = {"url":url, "parameters":kwargs}
    else:
      raise QueryTypeNotFound()

  def get_json(self):
    return requests.get(self.request['url'],self.request['parameters']).json()


class QueryTypeNotFound(Exception):
  def __init__(self,*args,**kwargs):
    Exception.__init__(self, args, kwargs) 