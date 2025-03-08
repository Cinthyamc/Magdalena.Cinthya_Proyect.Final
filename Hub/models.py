from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
#User = get_user_model()

class Post(models.Model):
    content = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)