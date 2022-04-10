from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


# Get the User Model
User = get_user_model()


class UserTests(APITestCase):
    def setUp(self):
        self.first_name = 'Gabriel'
        self.last_name = 'Santos'
        self.username = 'gabriel'
        self.email = 'gabriel@tsl.io.br'
        self.password = 'useruser'

        self.user = User.objects.create_user(
            first_name=self.first_name,
            last_name=self.last_name,
            username=self.username,
            email=self.email,
            password=self.password,
        )

    def test_credentials(self):
        url = reverse('token_obtain_pair')
        data = {
            'username': self.username,
            'password': self.password,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_wrong_credentials(self):
        url = reverse('token_obtain_pair')
        data = {
            'username': self.username,
            'password': 'wrongpassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_can_register(self):
        """
        Ensure we can create a new user.
        """
        url = reverse('users-list')
        data = {
            'first_name': 'Another User name',
            'last_name': 'Another User last name',
            'username': 'username',
            'email': 'username@email.com',
            'password': 'asdf@asdf',
            'confirm_password': 'asdf@asdf',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIs(User.objects.filter(username=self.username).exists(), True)


    def test_user_cannot_register(self):
        """
        Ensure we cannot register twice.
        """
        url = reverse('users-list')
        data = {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'confirm_password': self.password,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_retrieve(self):
        """
        Ensure we can retrieve an user details.
        """
        url = reverse('user-details', args=[self.user.pk])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_retrieve(self):
        """
        Ensure we get 404 in an unexistence user.
        """
        url = reverse('user-details', args=[0])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
