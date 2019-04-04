from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Post
from .models import Review

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['headline', 'price', 'content']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'review_text', 'score']