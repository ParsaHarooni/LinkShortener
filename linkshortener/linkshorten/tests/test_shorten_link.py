from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

USER_MODEL = get_user_model()
SHORTEN_URL = reverse("shorten_link")


def create_user(username, email, password):
    return USER_MODEL.objects.create_user(username=username, email=email, password=password)


class TestRegister(TestCase):
    def setUp(self) -> None:
        """
        Create 2 users and authenticate to the first account
        """
        self.client = APIClient()
        self.user = create_user(username="user", email="user@user.com", password="user")
        self.user_2 = create_user(username="user2", email="user2@user.com", password="user2")
        self.client.force_authenticate(self.user)

    def test_shorten_link_with_hash(self):
        """
        This test is to check if link is shortened with provided hash
        """
        resp = self.client.post(SHORTEN_URL, data=dict(url="http://test.com", hash="test"))
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_shorten_link_without_hash(self):
        """
        This test is to check if link is shortened without provided hash
        """
        resp = self.client.post(SHORTEN_URL, data=dict(url="http://test.com"))
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_shorten_link_hash_duplicate(self):
        """
        This test is to check if link is shortened if the hash is duplicate
        """
        self.client.post(SHORTEN_URL, data=dict(url="http://test.com", hash="test"))
        self.client.force_authenticate(self.user_2)
        resp = self.client.post(SHORTEN_URL, data=dict(url="http://test.com", hash="test"))
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_shorten_link_without_authentication(self):
        """
        This test is to check if link is shortened without authentication
        """
        client = APIClient()
        resp = client.post(SHORTEN_URL, data=dict(url="http://test.com"))
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_shorten_link_url_not_provided(self):
        """
        This test is to check if link is shortened without url provided
        """
        resp = self.client.post(SHORTEN_URL, data=dict())
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
