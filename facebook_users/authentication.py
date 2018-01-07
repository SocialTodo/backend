from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.exceptions import PermissionDenied
from django.conf import settings
import json
import os
import requests


class FacebookBackend(object):
  def authenticate(self, request, token=None):
    facebook_graph_response = requests.get(
        "https://graph.facebook.com/debug_token",
        params={
            "input_token": token,
            "access_token": os.environ["SOCIAL_TODO_APP_ID"] +
            "|" +
            os.environ["SOCIAL_TODO_APP_SECRET"]})
    fb_graph_dictionary = facebook_graph_response.json()
    import pdb; pdb.set_trace()  # breakpoint 282463a0 //

    if fb_graph_dictionary["data"]["is_valid"] and fb_graph_dictionary["data"]["user_id"] == json.loads(request.body)["UserID"]:
      user,created = User.objects.get_or_create(facebook_user_id = fb_graph_dictionary["data"]["user_id"], facebook_token = json.loads(request.body)["Token"])
      if created:
        user.set_unusable_password()
      return user
    elif not fb_graph_dictionary["data"]["is_valid"]:
      raise PermissionDenied
    return None


  def get_user(self,user_id):
    try:
      return User.objects.get(pk=user_id)
    except User.DoesNotExsist:
      return None

# class AuthenticateToken(authentication.BaseAuthentication):
#  def authenticate(self,request):
