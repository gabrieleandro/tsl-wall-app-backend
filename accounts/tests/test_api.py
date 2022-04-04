from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase


class UserTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'willsmith', 'will.smith@tsl.io.br', 'useruser')

    def test_user_register(self):
        """
        Ensure we can create a new user.
        """
        url = reverse('users-list')
        data = {
            'username': 'chrisrock',
            'email': 'chris.rock@tsl.io.br',
            'password': 'useruser',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIs(User.objects.filter(username='chrisrock').exists(), True)

    def test_user_details(self):
        """
        Ensure we can retrieve a user.
        """
        url = reverse('user-details', args=[1,])
        response = self.client.get(url)
        self.assertEqual(response.data, {'id': self.user.id, 'username': self.user.username})
