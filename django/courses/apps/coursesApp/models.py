from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['name']) < 6:
            errors['name'] = 'Name should be more than 5 charaters'
        if len(postData['desc']) < 16:
            errors['desc'] = 'Description should be more than 15 charaters'
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseManager()
