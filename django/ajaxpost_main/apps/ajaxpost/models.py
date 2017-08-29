from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):         # provides human readable version of output
        return self.post