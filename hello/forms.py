from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Post
from .models import Review
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['headline', 'price', 'content']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'review_text', 'score']

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))