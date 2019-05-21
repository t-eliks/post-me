from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

CATEGORIES = (
    ('electronics', 'Electronics'),
    ('kitchen', 'Kitchen'),
    ('transportation', 'Transportation'),
)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default = 0)
    headline = models.CharField(max_length=200, default="Post without title")
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    content = models.TextField()
    rating = models.IntegerField(default=0)
    publish_date = models.DateField("Published on", auto_now_add=True)
    category = models.CharField(choices=CATEGORIES, max_length=30)
    def __str__(self):
        return str(self.id)  + " " + self.headline
  
class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reviews', blank=True, null=True)
    reviewAuthor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default = 0)
    headline = models.CharField(max_length=200, default="Review")
    review_text = models.TextField()
    score = models.IntegerField(default=1, validators=[MinValueValidator(1),MaxValueValidator(5)])
    publish_date = models.DateField("Published on", auto_now_add=True, null=True)
    def __str__(self):
        return str(self.id)  + " " + self.headline