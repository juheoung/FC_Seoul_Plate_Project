from django.contrib.auth.models import User
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase

from bookmarks.models import BookMark
from restaurant.models import Restaurant


class BookMarkTestCode(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username='adasd',
            password='12345'
        )

    def test_bookmark_create(self):
        self.client.force_authenticate(user=self.user)
        res = Restaurant.objects.get(pk=1)
        data = {
            'restaurant': res,
        }
        response = self.client.post('/api/bookmark/', data=data)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['id'])
        self.assertEqual(response.data['restaurant'], data['restaurant'])

    def test_bookmark_delete(self):
        self.client.force_authenticate(user=self.user)
        bookmark = BookMark.objects.create(
            restaurant='1'
        )
        response = self.client.delete(f'/api/bookmark/{bookmark.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BookMark.objects.filter(pk=bookmark.id).count(), 0)

    def test_bookmark_duplicate(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'restaurant': '1'
        }
        response = self.client.post('/api/bookmark/', data=data)
        print(response)
        response2 = self.client.post('/api/bookmark/', data=data)
        self.assertEqual(BookMark.objects.filter(
            restaurant=data['restaurant'],
            bookmarks=self.user,
        ).count(), 1)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response2.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
