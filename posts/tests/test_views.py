from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Post


# Get the User Model
User = get_user_model()


from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


# Get the User Model
User = get_user_model()


class PostTests(APITestCase):
    def setUp(self):
        self.user_A = User.objects.create_user(
            username='tester_a',
            email='tester_a@tsl.io',
            password='password',
        )

        self.user_B = User.objects.create_user(
            username='tester_b',
            email='tester_b@tsl.io',
            password='password',
        )

        self.post_A = Post.objects.create(
            body='My new post user A.',
            author=self.user_A,
        )
        self.post_B = Post.objects.create(
            body='My new post user B.',
            author=self.user_B,
        )
    
    def test_guest_cannot_post_in_the_wall(self):
        """
        Ensure a guest user can't post in the wall.
        """
        url = reverse('posts-list')
        data = {
            'body': 'My new post.',
            'author_id': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_can_post_in_the_wall(self):
        """
        Ensure an authenticated user can post in the wall.
        """
        url = reverse('posts-list')
        data = {
            'author_id': self.user_A.pk,
            'body': 'My new post.',
        }
        self.client.force_authenticate(self.user_A)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Post.objects.filter(body='My new post.', author=self.user_A).exists())

    def test_empty_post_body(self):
        """
        Ensure we can't post empty body posts.
        """
        url = reverse('posts-list')
        data = {
            'author_id': self.user_A.pk,
            'body': '',
        }
        self.client.force_authenticate(self.user_A)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_authenticated_can_delete(self):
        """
        Ensure an authenticated user can delete posts.
        """
        url = reverse('post-details', args=[self.post_A.pk])
        self.client.force_authenticate(self.user_A)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Post.objects.filter(pk=self.post_A.pk).exists())
    
    def test_authenticated_cannot_delete_if_not_owner(self):
        """
        Ensure an authenticated user can only delete his own posts.
        """
        url = reverse('post-details', args=[self.post_A.pk])
        self.client.force_authenticate(self.user_B)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Post.objects.filter(pk=self.post_A.pk).exists())

    def test_guest_cannot_delete(self):
        """
        Ensure guests users can't delete any post.
        """
        url = reverse('post-details', args=[self.post_B.pk])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertTrue(Post.objects.filter(pk=self.post_B.pk).exists())
