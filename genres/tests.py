from django.test import TestCase
from ninja.testing import TestClient
from .api import router

class GenresTest(TestCase):
  def test_empty_result(self):
    client = TestClient(router)
    response = client.get("/")

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json(), [])