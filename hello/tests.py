from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, Client

from .views import index, detail, user_register, user_login, publishPost, categories, display_posts_by_category
from .models import Post, CATEGORIES

class GET_INDEX(TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

class GET_DETAIL(TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        author = User(username="a",password="b")
        author.save()
        post = Post(author=author)
        post.save()

        posts = Post.objects.all()

        response = self.client.get("/" + str(posts[0].id), follow=True)

        self.assertEqual(response.status_code, 200)

class GET_USER_REGISTER(TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.get('/register')

        self.assertEqual(response.status_code, 200)

class GET_USER_LOGIN(TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):

        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

class GET_DISPLAY_POSTS_BY_CATEGORY(TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        categories = CATEGORIES[0][0]

        response = self.client.get('/categories/' + str(categories) + "/")

        self.assertEqual(response.status_code, 200)

class GET_CATEGORIES(TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.get('/categories/')

        self.assertEqual(response.status_code, 200)

class GET_PUBLISH_POST_ANONYMOUS(TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.get('/publish/', follow=True)
        self.assertEqual(response.status_code, 401)

class GET_PUBLISH_POST_LOGGED_IN(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

    def test_details(self):
        response = self.client.get('/publish/', follow=True)
        self.assertEqual(response.status_code, 200)