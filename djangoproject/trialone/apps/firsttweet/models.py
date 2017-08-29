from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ApiKey(models.Model):
    """
    Keys for accessing the Twitter Streaming API.
    """

    created_at = models.DateTimeField(auto_now_add=True)

    user_name = models.CharField(max_length=250)
    app_name = models.CharField(max_length=250)
    email = models.EmailField(default=None, blank=True)

    api_key = models.CharField(max_length=250)
    api_secret = models.CharField(max_length=250)

    access_token = models.CharField(max_length=250)
    access_token_secret = models.CharField(max_length=250)