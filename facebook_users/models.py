from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class FacebookUser(AbstractBaseUser):
    facebook_user_id = models.CharField(max_length=300, unique=True, db_index=True, primary_key=True)
    facebook_token = models.CharField(max_length=700)

    USERNAME_FIELD = 'facebook_user_id'

    def __str__(self):
        return self.facebook_user_id


# class FacebookBackend:
#     def authenticate(self, request, token=None):
#         if(authenticate_facebook_user(token)):
#             try:
#                 return User.objects.get(user_id=user_id)
#             except User.DoesNotExist:
#                 return User.objects.create_user(
#                     None, None, None, user_id=user_id, token=token)
#         else:
#             raise PermissionDenied

#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# from django.db import models


# class FacebookUserManager(BaseUserManager):
#     def create_user(self,user_id,token,expiration):
#         if not user_id or not token or not expiration:
#             raise ValueError("User creation missing a required field")
#         user = User.objects.create(user_id=user_id,token=token,expiration=expiration)
#         user.set_unusable_password()
#         user.save()
#         return user

#     def update_token(self,user_id,token,expiration):
#         return


# # I promise I will refactor this when it all works
