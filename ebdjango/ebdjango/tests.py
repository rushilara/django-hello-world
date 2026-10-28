from django.test import SimpleTestCase
from django.urls import reverse


class HelloViewTests(SimpleTestCase):
    def test_hello_returns_greeting(self):
        response = self.client.get(reverse("hello"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Hello, world!")
