from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from ..serializers import PostSerializer


# Get the User Model
User = get_user_model()


class TestPostSerializer(APITestCase):
    def setUp(self):
        self.Serializer = PostSerializer

        self.user = User.objects.create_user(
            username='tester',
            email='tester@tsl.io',
            password='password',
        )

    def test_is_valid(self):
        data = {
            'author': self.user.pk,
            'body': 'My new post.',
        }
        serializer = self.Serializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors, {})

    def test_empty_body_message(self):
        """
        Ensure if any field is missing, serializer should not validate
        """
        data = {
            'author_id': 1,
            #'body': 'My new post.', # Missing field
        }
        serializer = self.Serializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('body', serializer.errors)
