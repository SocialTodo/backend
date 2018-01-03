from django.db import models
from django.contrib.auth.models import (
    User,
    AbstractBaseUser,
    BaseUserManager
)
import requests
import os
from django.core.exceptions import PermissionDenied

# Create your models here.

class FacebookUser(AbstractBaseUser):
    user_id = models.CharField(max_length=300)
    token = models.CharField(max_length=700)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['token']

    def __str__(self):
        return self.user_id

class FacebookUserManager(BaseUserManager):
    def create_user(self,user_id,token,expiration):
        if not user_id or not token or not expiration:
            raise ValueError("User creation missing a required field")
        user = User.objects.create(user_id=user_id,token=token,expiration=expiration)
        user.set_unusable_password()
        user.save()
        return user

    def update_token(self,user_id,token,expiration):
        return

class FacebookLogin:
    def authentication(self, request, user_id = None, token=None):
        if(authenticate_user(user_id,token)):
            try:
                return User.objects.get(user_id=user_id)
            except User.DoesNotExist:
                return User.objects.create_user(None,None,None,user_id=user_id,token=token)
        else:
            raise PermissionDenied

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None




# I promise I will refactor this when it all works
def authenticate_user(user_id,token):
    facebook_graph_response = requests.get("https://graph.facebook.com/debug_token", \
                                           params={"input_token": token, \
                                                   "access_token": os.environ["SOCIAL_TODO_APP_ID"] \
                                                                   + "|" \
                                                                   + os.environ["SOCIAL_TODO_APP_SECRET"]})
    if facebook_graph_response.json()["data"]["is_valid"] == True:
        # ALSO CHECK user_id's MATCH!
        print(facebook_graph_response.json())