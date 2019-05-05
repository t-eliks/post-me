from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Post
from .models import Review
from django import forms
from django.utils.translation import ugettext_lazy as _

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['headline', 'price', 'content']
        widgets = {
            'headline': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'headline': _('Antraštė'),
            'content': _('Turinys'),
            'price': _('Kaina'),
        }

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'review_text', 'score']
        widgets = {
            'headline': forms.TextInput(attrs={'class': 'form-control'}),
            'review_text': forms.Textarea(attrs={'class': 'form-control'}),
            'score': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'headline': _('Antraštė'),
            'review_text': _('Atsiliepimas'),
            'score': _('Įvertis'),
        }

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))