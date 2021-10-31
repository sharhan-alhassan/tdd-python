from django.test import TestCase
from .views import home_page
from django.urls import resolve

# Create your tests here.

class HomePageTest(TestCase):
    """resolve is the function Django uses internally to resolve 
    URLs and find what view function they should map to
    """
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)