from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    publish_date = models.DateField("Published on", auto_now_add=True)