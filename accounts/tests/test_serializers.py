from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from ..serializers import UserSerializer, AuthorSerializer


# Get the User Model
User = get_user_model()


class TestUserSerializer(APITestCase):
    def setUp(self):
        self.Serializer = UserSerializer

    def test_is_valid(self):
        data = {
            'first_name': 'Tester',
            'last_name': 'Beta',
            'username': 'tester',
            'email': 'tester@tsl.io',
            'password': 't3st3rpass',
            'confirm_password': 't3st3rpass',
        }
        serializer = self.Serializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors, {})

    def test_it_should_not_validate_if_any_fields_missing(self):
        """
        Ensure if any field is missing, serializer should not validate
        """
        data = {
            'first_name': 'Tester',
            'last_name': 'Beta',
            # 'username': 'tester', # Missing field
            'email': 'tester@tsl.io',
            'password': 't3st3rpass',
            'confirm_password': 't3st3rpass',
        }
        serializer = self.Serializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('username', serializer.errors)

    def test_author(self):
        data = {
            'first_name': 'Tester',
            'last_name': 'Beta',
            'username': 'tester',
            'email': 'tester@tsl.io',
            'password': 't3st3rpass',
            'confirm_password': 't3st3rpass',
        }
        serializer = AuthorSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertIn('first_name', serializer.validated_data)
        self.assertIn('last_name', serializer.validated_data)
        self.assertIn('username', serializer.validated_data)
        self.assertNotIn('email', serializer.validated_data)
