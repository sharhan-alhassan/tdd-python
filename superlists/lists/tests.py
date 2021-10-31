


from django.http import response, HttpRequest
from django.test import TestCase
from .views import home_page
from django.urls import resolve

# Create your tests here.

class HomePageTest(TestCase):
    """
    Unit testing a url resolution to a function

    resolve is the function Django uses internally to resolve 
    URLs and find what view function they should map to
    """
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        res = home_page(request)
        html = res.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
        