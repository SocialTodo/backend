from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class FacebookUser(AbstractBaseUser):
    facebook_user_id = models.CharField(
        max_length=300,
        unique=True,
        db_index=True,
        primary_key=True)
    facebook_token = models.CharField(max_length=700)
    facebook_friends = models.ManyToManyField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=255)

    USERNAME_FIELD = 'facebook_user_id'
    REQUIRED_FIELDS = ['name']


    def __str__(self):
        return self.facebook_user_id

    def set_friends(self, friends):
        for friend in friends:
            self.facebook_friends.add(friend)
        self.save()


