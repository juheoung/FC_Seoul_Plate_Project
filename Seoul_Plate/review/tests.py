from django.test import TestCase

# Create your tests here.
from model_bakery import baker
from munch import Munch
from rest_framework import status
from rest_framework.test import APITestCase

from review.models import Review


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.test_review = baker.make(Review,
                                      review_image='https://rforcats.net/assets/img/programmer.png',
                                      taste_value='GOOD',
                                      review_text='taste testing')

    def test_should_list_review(self):
        # self.client.force_authenticate(user=self.testAccount)
        response = self.client.get('/api/reviews/')

        print(self.test_review.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        review_response = Munch(response.data)
        self.assertTrue(review_response.id)
        self.assertEqual(review_response.review_text, self.test_review.review_text)
        self.assertEqual(review_response.revies_image, self.test_review.image)
        self.fail()
