import random

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from linkshorten.tests.test_shorten_link import create_user

GET_ALL_URL = reverse('get_all')
SHORTEN_URL = reverse("shorten_link")

DESKTOP_USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) ' \
                     'Chrome/1.0.154.53 Safari/525.19 '

ANDROID_USER_AGENT = 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, ' \
                     'like Gecko) Version/4.0 Mobile Safari/534.30 '


class TestGetAllAnalytics(TestCase):
    def setUp(self) -> None:
        self.api_client = APIClient()
        self.client = Client()
        self.user = create_user(username="user", email="user@user.com", password="user")
        self.api_client.force_authenticate(self.user)

    def test_get_analytics(self):
        shorten_resp = self.api_client.post(SHORTEN_URL, data=dict(url="http://test.com")).json()
        url_hash = shorten_resp['hash']
        shorten_url = shorten_resp['shorten_url']
        for _ in range(0, 100):
            self.client.get(shorten_url, HTTP_USER_AGENT=DESKTOP_USER_AGENT)
            self.client.get(shorten_url, HTTP_USER_AGENT=ANDROID_USER_AGENT)
        resp = self.api_client.get(GET_ALL_URL, data=dict(hash=url_hash))
        self.assertEqual(resp.status_code, 200)
