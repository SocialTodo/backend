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

    USERNAME_FIELD = 'facebook_user_id'

    def __str__(self):
        return self.facebook_user_id
