from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post

# Create your tests here.


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="ubuntu", email="ubuntu@gmail.com", password="debian"
        )

        self.post = Post.objects.create(
            title="A good day to die",
            author=self.user,
            body="Somebody save me from this nightmare",
        )

    def test_string_representation(self):
        post = Post(title="A sample title")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "A good day to die")
        self.assertEqual(f"{self.post.author}", "ubuntu")
        self.assertEqual(f"{self.post.body}", "Somebody save me from this nightmare")

    def test_post_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Somebody save me from this nightmare")
        self.assertTemplateUsed(response, "home.html")

    def test_post_detail_view(self):
        response = self.client.get("/post/1/")
        no_response = self.client.get("/post/100/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A good day to die")
        self.assertTemplateUsed(response, "blog/post_detail.html")
