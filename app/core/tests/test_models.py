from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
     
    def test_create_sample_user(self):
        """Test creating sample user"""
        username = "user"
        password="pass1234"
        user = get_user_model().objects.create_user(
                username = username,
                password = password
                )
