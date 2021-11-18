from django.db import models
from django.db.models.base import Model

class Private(models.Model):
    is_private = models.BooleanField(default=True)
    message = models.TextField(default='you are getting response because you are authenticated.')


class Public(models.Model):
    is_public = models.BooleanField(default=True)
    message = models.TextField(default='You are getting response wether you are authenticated or not because this response is public.')
