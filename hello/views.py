from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.defaulttags import register

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Greeting, Post, Review, CATEGORIES

from .forms import PostForm, ReviewForm, RegisterForm


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# Create your views here.
def index(request):
    search_term = ''

    if 'search' in request.GET:
        search_term = request.GET['search']
        posts = Post.objects.filter(headline__contains=search_term)
    else:
        posts = Post.objects.order_by('-publish_date')[:5]

    context = {
        'posts': posts,
        'categories': dict(CATEGORIES)
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

#@login_required(login_url='/login')
def publishPost(request):
    if request.user.is_authenticated is False:
        return render(request, 'hello/publish.html', status=401)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.author = request.user
            f.save()

            return HttpResponseRedirect('/')

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

def user_login(request):
    template = '../templates/registration/login.html'
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    
    return render(request,template)

def categories(request):
    categories = []

    for var in range(len(CATEGORIES)):
        categories.append(CATEGORIES[var][1])

    context = {
        'categories': categories
    }
    return render(request, 'hello/categories.html', context)

def display_posts_by_category(request, category):
    posts = Post.objects.filter(category=category)
    context = {
        'posts': posts,
        'category_name': dict(CATEGORIES).get(category),
        'categories': dict(CATEGORIES)
    }
    return render(request, 'hello/categorized_list.html', context)
