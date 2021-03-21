from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import resolve, reverse
# Create your tests here.


class HomepageViewTest(SimpleTestCase):
    def test_homepage_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_about_view_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
