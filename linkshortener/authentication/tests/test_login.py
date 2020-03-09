from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

LOGIN_URL = reverse("login")
USER_MODEL = get_user_model()


class TestLogin(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = USER_MODEL.objects.create_user(username="user", email="user@user.com", password="useruser")

    def test_login_successfully(self):
        """
        This test is for checking if user is logged in correctly
        Should return 200 as response
        """
        resp = self.client.post(LOGIN_URL, data=dict(username="user", password="useruser"))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_login_with_invalid_credential(self):
        """
        This test is for checking that is not logged in with incorrect credentials
        Should return 400 as response
        """
        resp = self.client.post(LOGIN_URL, data=dict(username="false", password="false"))
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_credential_not_provided(self):
        """
        This test is for checking if user is logged in if credentials are not provided
        Should return 400 as response
        """
        resp = self.client.post(LOGIN_URL, data=dict())
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
