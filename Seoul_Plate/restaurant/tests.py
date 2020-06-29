from django.test import TestCase
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase


class RestaurantTestCase(APITestCase):
    def setUp(self) -> None:
        self.restaurant_size = 3
        self.test_restaurant = baker.make('restaurant.Restaurant', _quantity=self.restaurant_size)

    def test_should_list_restaurant(self):
        """
        Request : GET - /api/restaurant/
        """
        response = self.client.get('/api/restaurant/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), self.restaurant_size)

        for test_rest, response_rest in zip(self.test_restaurant, response.data['results']):
            self.assertEqual(test_rest.id, response_rest['id'])
            self.assertEqual(test_rest.rest_name, response_rest['rest_name'])
            # serializer 에서 선언한 필드가 정확히 response 되는지 확인 필요

    def test_should_detail_restaurant(self):
        """
        Request : GET - /api/restaurant/{restaurant_id}
        """
        test_restaurant = self.test_restaurant[0]
        response = self.client.get(f'/api/restaurant/{test_restaurant.id}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(test_restaurant.id, response.data['id'])
        # serializer 에서 선언한 필드가 정확히 response 되는지 확인 필요
