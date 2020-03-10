from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from linkshorten.models import Link

USER_MODEL = get_user_model()


class RedirectTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        user = USER_MODEL.objects.create_user(username="user", email="user@user.com", password="test")
        self.shorten_hash = Link.shorten_link(url="http://google.com", user=user, url_hash="test").hash

    def test_redirect_not_found(self):
        """
        This test is to check not redirecting the invalid urls
        Should return 404 as Response
        """
        url = reverse('redirect', args=["testtest"])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_redirect_successfully(self):
        """
        This test is to check not redirecting the urls
        Should return 302 as Response
        """
        url = reverse('redirect', args=["test"])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_302_FOUND)
