from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


# Get the User Model
User = get_user_model()


class UserTests(APITestCase):
    def setUp(self):
        self.username = 'gabriel'
        self.email = 'gabriel@tsl.io.br'
        self.password = 'useruser'

        # self.user = User.objects.create_user(
        #     username=self.username,
        #     email=self.email,
        #     password=self.password,
        # )

    def test_user_register(self):
        """
        Ensure we can create a new user.
        """
        url = reverse('users-list')
        data = {
            'username': self.username,
            'email': self.email,
            'password': self.password,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response2 = self.client.post(url, data, format='json')
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertIs(User.objects.filter(username=self.username).exists(), True)

    # def test_user_can_authenticate(self):
