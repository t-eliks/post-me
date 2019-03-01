from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-publish_date')[:5]
    context = {
        'posts': posts,
    }
    return render(request, 'hello/index.html', context)
