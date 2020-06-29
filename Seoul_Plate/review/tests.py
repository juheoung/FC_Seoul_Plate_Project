from django.contrib.auth.models import User
# Create your tests here.
from model_bakery import baker
from munch import Munch
from rest_framework import status
from rest_framework.test import APITestCase

from restaurant.models import Restaurant
from review.models import Review


class ReviewTestCase(APITestCase):
    def setUp(self) -> None:
        """
        Ready before test
        Create random reviews(3) , random user(1), random restaurant(1)
        """
        self.test_user = User.objects.create(username="test", password="1111")
        self.test_reviews = baker.make('review.Review', _quantity=3)
        self.test_restaurant = Restaurant.objects.create()
        self.review = Review.objects.create(review_text="for delete",
                                            owner_rest=self.test_restaurant,
                                            owner_user=self.test_user,
                                            taste_value="SOSO")

    def test_should_get_review(self):
        """
        Detail review information
        Request : GET - /api/reviews/{review_id}
        """
        test_review = self.test_reviews[0]
        self.client.force_authenticate(user=test_review)
        # trailing slash 설정 변경 필요
        response = self.client.get(f'/api/reviews/{test_review.id}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], test_review.id)
        self.assertEqual(response.data['review_text'], test_review.review_text)
        self.assertEqual(response.data['review_image'], test_review.review_image)

    def test_should_create_review(self):
        # nested router 사용
        # https://github.com/alanjds/drf-nested-routers
        # ex) POST - /api/restaurant/123/reviews
        # ex) POST users/123/posts/456/comments/678/likes/999
        # ex) DELETE /likes/999

        """
        Request : POST - /api/reviews/
        """
        data = {"review_text": "new review",
                # "review_image": None,
                "taste_value": "SOSO",
                "owner_rest": self.test_restaurant.id,
                "owner_user": self.test_user.id,
                }
        self.client.force_authenticate(user=self.test_user)
        response = self.client.post('/api/reviews/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        review_response = Munch(response.data)
        self.assertTrue(review_response.id)
        self.assertEqual(review_response.review_text, data['review_text'])
        # self.assertEqual(review_response.review_image, data['review_image'])

        print(response.data)

        self.fail()

    def test_should_delete_review(self):
        """
        Request : DELETE - /api/reviews/
        """
        self.client.force_authenticate(user=self.test_user)
        test_review = self.test_reviews[0]
        entry = Review.objects.get(id=self.review.id)
        self.client.force_authenticate(user=self.test_user)
        response = self.client.delete(f'/api/reviews/{self.review.id}')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Review.objects.filter(id=entry.id).exists())

    def test_should_update_review(self):
        """
        Request : PUT - /api/reviews/{review_id}
        """
        prev_text = self.review.review_text
        prev_taste_value = self.review.taste_value
        data = {"review_text": "updated review",
                # "review_image": None,
                "taste_value": "GOOD",
                "owner_rest": self.test_restaurant.id,
                "owner_user": self.test_user.id,
                }
        self.client.force_authenticate(user=self.test_user)
        response = self.client.put(f'/api/reviews/{self.review.id}', data=data)

        review_response = Munch(response.data)
        self.assertTrue(review_response.id)
        self.assertNotEqual(review_response.review_text, prev_text)
        self.assertNotEqual(review_response.taste_value, prev_taste_value)

    def test_should_patch_review(self):
        """
        Request : PATCH - /api/reviews/{review_id}
        """
        prev_text = self.review.review_text
        prev_taste_value = self.review.taste_value
        data = {"review_text": "patched review",
                "taste_value": "BAD",
                }
        self.client.force_authenticate(user=self.test_user)
        response = self.client.patch(f'/api/reviews/{self.review.id}', data=data)

        review_response = Munch(response.data)
        self.assertTrue(review_response.id)
        self.assertNotEqual(review_response.review_text, prev_text)
        self.assertNotEqual(review_response.taste_value, prev_taste_value)
