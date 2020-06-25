from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.users = baker.make('auth.User', _quantity=3)

    def test_list(self):
        """
        All review list
        Request : GET - /api/users/
        """
        user = self.users[0]
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for user_response, user in zip(response.data, self.users):
            self.assertEqual(user_response['id'], user.id)
            self.assertEqual(user_response['username'], user.username)
            self.assertEqual(user_response['email'], user.email)
        self.fail()
    def test_detail(self):
        self.fail()

    def test_create(self):
        self.fail()

    def test_delete(self):
        self.fail()

    def test_update(self):
        self.fail()

    def test_login(self):
        self.fail()

    def test_logout(self):
        self.fail()
