from django.test import TestCase
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase


class RestaurantTestCase(APITestCase):
    def setUp(self) -> None:
        self.test_restaurant = baker.make('restaurant.Restaurant', _quantity=3)

    def test_should_list_restaurant(self):
        response = self.client.get('/api/restaurant/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for test_rest, response_rest in zip(self.test_restaurant, response.data):
            print(response_rest)
            self.assertEqual(test_rest.id, response_rest['id'])
            self.assertEqual(test_rest.rest_name, response_rest['rest_name'])
        self.fail()

    def test_should_detail_restaurant(self):
        test_restaurant = self.test_restaurant[0]
        response = self.client.get(f'/api/restaurant/{test_restaurant.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.fail()
