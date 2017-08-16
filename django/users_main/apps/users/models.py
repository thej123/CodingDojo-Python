from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255, min_length=4)
    last_name = models.CharField(max_length=255, min_length=4)
    email = models.EmailField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
