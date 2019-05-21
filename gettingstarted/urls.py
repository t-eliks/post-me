from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

urlpatterns = [
    path("", hello.views.index, name="index"),
    # ex: .../penktas postas/
    path('<int:post_id>/', hello.views.detail, name='detail'),
    path("publish/", hello.views.publishPost, name='publish'),
    path("accounts/", include('django.contrib.auth.urls')),
    path("admin/", admin.site.urls),
    path("login", hello.views.user_login, name="user_login"),
    path("register", hello.views.user_register, name='user_register'),
    path("categories/", hello.views.categories, name='categories'),
    path("categories/<str:category>/", hello.views.display_posts_by_category),
]

