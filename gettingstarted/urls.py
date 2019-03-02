from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("accounts/", include('django.contrib.auth.urls')),
    path("admin/", admin.site.urls),
    path("accounts/login/", include('django.contrib.auth.urls')),
]
