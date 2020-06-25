from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from model_bakery import baker
from munch import Munch
from rest_framework import status
from rest_framework.test import APITestCase

from restaurant.models import Restaurant
from review.models import Review


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.test_reviews = baker.make('review.Review', _quantity=3)
        self.test_user = User.objects.create(username="test", password="1111")
        self.test_restaurant = Restaurant.objects.create()

    def test_should_list_review(self):
        # self.client.force_authenticate(user=self.testAccount)
        response = self.client.get('/api/reviews/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for response_review, origin_review in zip(response.data, self.test_reviews):
            self.assertEqual(response_review['id'], origin_review.id)
            self.assertEqual(response_review['review_text'], origin_review.review_text)
            self.assertEqual(response_review['review_image'], origin_review.review_image)

    def test_should_get_review(self):
        test_review = self.test_reviews[0]
        self.client.force_authenticate(user=test_review)
        response = self.client.get(f'/api/reviews/{test_review.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], test_review.id)
        self.assertEqual(response.data['review_text'], test_review.review_text)
        self.assertEqual(response.data['review_image'], test_review.review_image)

    def test_should_create_review(self):
<<<<<<< HEAD
        login_data = {
            "username": self.test_user['username'],
            "password": "12345",
        }
=======
        data = {"review_text": "new review",
                #"review_image": None,
                "taste_value": "SOSO",
                "owner_rest": self.test_restaurant.id,
                "owner_user": self.test_user.id,
                }
        self.client.force_authenticate(user=self.test_user)

        response = self.client.post('/api/reviews/', data=data)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.data)
        review_response = Munch(response.data)
        self.assertTrue(review_response.id)
        self.assertEqual(review_response.review_text, data['review_text'])
        # self.assertEqual(review_response.review_image, data['review_image'])
        self.fail()
>>>>>>> 33e3eae3902572e409ac62368be848393b69cb84

    def test_should_delete_review(self):
        test_review = self.test_reviews[0]
        response = self.client.delete(f'/api/reviews/{test_review.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.fail()
