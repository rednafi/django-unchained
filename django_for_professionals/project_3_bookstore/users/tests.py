from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser", email="testuser@testmail.com", password="testpass",
        )

        self.assertEquals(user.username, "testuser")
        self.assertEquals(user.email, "testuser@testmail.com")
        self.assertEquals(user.password, "testpass")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()

        admin_user = User.objects.create_superuser(
            username="superadmin", email="superadmin@email.com", password="superpass"
        )

        self.assertEquals(admin_user.username, 'superadmin')
        self.assertEquals(admin_user.email, 'superadmin@email.com')
        self.assertEqual(admin_user.password, 'superpass')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        