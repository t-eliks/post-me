from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory

from .views import index, detail, user_register, user_login, publishPost, categories, display_posts_by_category
from .models import Post, CATEGORIES

class GET_INDEX(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_details(self):
        request = self.factory.get("/")
        request.user = AnonymousUser()

        response = index(request)
        self.assertEqual(response.status_code, 200)

class GET_DETAIL(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_details(self):
        request = self.factory.get("/detail")
        request.user = AnonymousUser()

        author = User(username="a",password="b")
        author.save()
        post = Post(author=author)
        post.save()

        posts = Post.objects.all()

        response = detail(request, posts[0].id)

        self.assertEqual(response.status_code, 200)

class GET_USER_REGISTER(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_details(self):
        request = self.factory.get("/detail")
        request.user = AnonymousUser()

        response = user_register(request)

        self.assertEqual(response.status_code, 200)

class GET_USER_LOGIN(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_details(self):
        request = self.factory.get("/detail")
        request.user = AnonymousUser()

        response = user_login(request)

        self.assertEqual(response.status_code, 200)

class GET_USER_REGISTER(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_details(self):
        request = self.factory.get("/detail")
        request.user = AnonymousUser()

        response = user_register(request)

        self.assertEqual(response.status_code, 200)

class GET_PUBLISH_POST(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_details(self):
        request = self.factory.get("/publish")
        request.user = AnonymousUser()

        response = publishPost(request)

        self.assertEqual(response.status_code, 200)

class GET_DISPLAY_POSTS_BY_CATEGORY(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_details(self):
        request = self.factory.get("/display_posts_by_category")
        request.user = AnonymousUser()

        categories = CATEGORIES[0]

        response = display_posts_by_category(request, categories)

        self.assertEqual(response.status_code, 200)

class GET_CATEGORIES(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_details(self):
        request = self.factory.get("/categories")
        request.user = AnonymousUser()

        response = categories(request)

        self.assertEqual(response.status_code, 200)