# pages/test.py
from django.test import TestCase #testeo con base de datos
from django.test import SimpleTestCase #testeo simple


# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
