from model_bakery import baker
from rest_framework.test import APITestCase


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = baker.make('auth.User', _quantity=3)

    def test_list(self):
        print(self.user[0])
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
