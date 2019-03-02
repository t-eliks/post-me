from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Greeting
from .models import Post
from .models import Review

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-publish_date')[:5]
    context = {
        'posts': posts,
    }
    return render(request, 'hello/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    reviews = post.reviews.all()
    context = {
        'post': post,
        'reviews': reviews

    }
    return render(request, 'hello/detail.html', context)
