from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
from posts.models import Post


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create a user
        test_user = User.objects.create(username="testuser", password="testpass")
        test_user.save()

        # create a blog
        test_blog = Post.objects.create(
            author=test_user, title="Test Title", body="Test body"
        )

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        body = f"{post.body}"

        self.assertEquals(author, "testuser")
        self.assertEquals(title, "Test Title")
        self.assertEquals(body, "Test body")
