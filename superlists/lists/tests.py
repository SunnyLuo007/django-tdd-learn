from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest


# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        content = response.content.decode(encoding='utf8')
        self.assertIn('To-Do', content)
        self.assertTemplateUsed(response, 'home.html')