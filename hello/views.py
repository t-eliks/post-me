from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .models import Greeting
from .models import Post
from .models import Review

from.forms import PostForm
from.forms import ReviewForm
from .forms import RegisterForm


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

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            newReview = form.save(commit=False)
            newReview.post = post
            newReview.reviewAuthor = request.user
            newReview.save()

    context = {
        'post': post,
        'reviews': reviews,
        'form': ReviewForm,
        'user': request.user
    }

    return render(request, 'hello/detail.html', context)

def publishPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.author = request.user
            f.save()

    context = {
        'form': PostForm
    }
    return render(request, 'hello/publish.html', context)

def user_register(request):
    # if this is a POST request we need to process the form data
    template = '../templates/registration/registration.html'
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                
                user.save()
                # Login the user
                login(request, user)
               
                # redirect to accounts page:
                return HttpResponseRedirect('/')
                
   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})