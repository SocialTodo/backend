from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FacebookUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facebookAuthenticationToken = models.CharField(max_length=700)
    facebookExpirationDate = models.DateTimeField()
    facebookUserID = models.CharField(max_length=100)
