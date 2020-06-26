from django.contrib.auth.models import User
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase

from bookmarks.models import BookMark
<<<<<<< HEAD
from restaurant.models import Restaurant
=======
>>>>>>> e1a79450099e1fb86b9e432320f59f27e8766aeb


class BookMarkTestCode(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username='adasd',
            password='12345'
        )
<<<<<<< HEAD
        self.restaurant = Restaurant.objects.create()

=======
>>>>>>> e1a79450099e1fb86b9e432320f59f27e8766aeb

    def test_bookmark_create(self):
        self.client.force_authenticate(user=self.user)
        data = {
<<<<<<< HEAD
            'restaurant': self.restaurant.id
        }
        response = self.client.post('/api/bookmark/', data=data)

=======
            'restaurant': '1'
        }
        response = self.client.post('/api/bookmark/', data=data)
        print(response)
>>>>>>> e1a79450099e1fb86b9e432320f59f27e8766aeb
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['id'])
        self.assertEqual(response.data['restaurant'], data['restaurant'])

    def test_bookmark_delete(self):
        self.client.force_authenticate(user=self.user)
<<<<<<< HEAD
        test_bookmark = BookMark.objects.create(bookmarks=self.user, restaurant=self.restaurant)
        entry = BookMark.objects.get(id=test_bookmark.id)

        response = self.client.delete(f'/api/bookmark/{test_bookmark.id}')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(BookMark.objects.filter(id=entry.id).exists())

=======
        bookmark = BookMark.objects.create(
            restaurant='1'
        )
        response = self.client.delete(f'/api/bookmark/{bookmark.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BookMark.objects.filter(pk=bookmark.id).count(), 0)
>>>>>>> e1a79450099e1fb86b9e432320f59f27e8766aeb

    def test_bookmark_duplicate(self):
        self.client.force_authenticate(user=self.user)
        data = {
<<<<<<< HEAD
            'restaurant': self.restaurant.id
        }
        response = self.client.post('/api/bookmark/', data=data)
        response2 = self.client.post('/api/bookmark/', data=data)

=======
            'restaurant': '1'
        }
        response = self.client.post('/api/bookmark/', data=data)
        print(response)
        response2 = self.client.post('/api/bookmark/', data=data)
>>>>>>> e1a79450099e1fb86b9e432320f59f27e8766aeb
        self.assertEqual(BookMark.objects.filter(
            restaurant=data['restaurant'],
            bookmarks=self.user,
        ).count(), 1)
<<<<<<< HEAD

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
=======
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
>>>>>>> e1a79450099e1fb86b9e432320f59f27e8766aeb
        self.assertEqual(response2.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

