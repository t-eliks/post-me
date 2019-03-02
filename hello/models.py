from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default = 0)
    headline = models.CharField(max_length=200, default="Skelbimas be pavadinimo")
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    content = models.TextField()
    publish_date = models.DateField("Published on", auto_now_add=True)
    def __str__(self):
        return str(self.id)  + " " + self.headline
  
class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reviews', blank=True, null=True)
    headline = models.CharField(max_length=200, default="Atsiliepimas")
    review_text = models.TextField()
    score = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(5)])
    publish_date = models.DateField("Published on", auto_now_add=True, null=True)
    def __str__(self):
        return str(self.id)  + " " + self.headline
