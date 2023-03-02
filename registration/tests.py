from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

class UserAccountTests(TestCase):
    def test_new_superuser(self):
        db=get_user_model()
        super_user=db.objects.create_superuser(
            'testuser@super.com','username','password')
        self.assertEqual(super_user.email, "testuser@super.com")
        self.assertEqual(super_user.username, "username")
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user),"username")

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com',username='username1',password='password',is_superuser=False
            )
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com',username='username1',password='password',is_staff=False
            )
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com',username='username1',password='password',is_active=False
            )