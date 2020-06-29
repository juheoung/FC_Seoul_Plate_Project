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
        self.users = baker.make('auth.User', _quantity=4)

        self.restaurant = Restaurant.objects.create()

    def test_bookmark_create(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'restaurant': self.restaurant.id
        }

        response = self.client.post('/api/bookmark/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['id'])
        self.assertEqual(response.data['restaurant'], data['restaurant'])

    def test_bookmark_delete(self):
        self.client.force_authenticate(user=self.user)
        test_bookmark = BookMark.objects.create(bookmarks=self.user, restaurant=self.restaurant)
        entry = BookMark.objects.get(id=test_bookmark.id)

        response = self.client.delete(f'/api/bookmark/{test_bookmark.id}')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(BookMark.objects.filter(id=entry.id).exists())

    def test_bookmark_duplicate(self):
        baker.make('bookmarks.BookMark', bookmarks=self.user, restaurant_id=self.restaurant.id)

        self.client.force_authenticate(user=self.user)
        data = {
            'restaurant': self.restaurant.id
        }
        # network 여러번 할 필요없이 필요한 환경을 강제로 설정
        # response = self.client.post('/api/bookmark/', data=data)

        response = self.client.post('/api/bookmark/', data=data)

        self.assertEqual(BookMark.objects.filter(
            restaurant=data['restaurant'],
            bookmarks=self.user,
        ).count(), 1)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # 필요없어 보임
    def test_bookmark_count(self):
        for i in range(3):
            self.client.force_authenticate(user=self.users[i])
            data = {
                'restaurant': self.restaurant.id
            }
            response = self.client.post('/api/bookmark/', data=data)

        self.assertEqual(BookMark.objects.filter(restaurant=self.restaurant).count(), 3)
