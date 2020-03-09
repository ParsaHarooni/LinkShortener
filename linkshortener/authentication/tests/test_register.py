from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

REGISTER_URL = reverse("register")


class TestRegister(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_create_user(self):
        """
        This test is for checking if user is correctly created
        Should return 201
        """
        resp = self.client.post(REGISTER_URL, data=dict(username="user", email="user@user.com", password="pass"))
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_create_user_duplicate_username(self):
        """
        This test is for checking if user is created if username is duplicate
        Should return 400
        """
        self.client.post(REGISTER_URL, data=dict(username="user", email="user@user.com", password="pass"))
        resp = self.client.post(REGISTER_URL, data=dict(username="user", email="user1@user.com", password="pass"))
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_duplicate_email(self):
        """
        This test is for checking if user is created if email is duplicate
        Should return 400
        """
        self.client.post(REGISTER_URL, data=dict(username="user", email="user@user.com", password="pass"))
        resp = self.client.post(REGISTER_URL, data=dict(username="user2", email="user@user.com", password="pass"))
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_credential_not_provided(self):
        """
        This test is for checking if user is created if credentials are not provided
        Should return 400
        """
        resp = self.client.post(REGISTER_URL, data=dict())
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
