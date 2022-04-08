from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Post


# Get the User Model
User = get_user_model()

class PostTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'willsmith',
            'will.smith@tsl.io.br',
            'useruser')
    
    def test_create_post(self):
        url = reverse('posts-list')
        data = {
            'body': 'first tsl wall post.',
            'author': self.user.pk,
        }
        self.client.login(username='willsmith', password='useruser')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertIs(Post.objects.get(body='first tsl wall post.').exists(), True)
