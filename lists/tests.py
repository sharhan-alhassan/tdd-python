


from django.http import response, HttpRequest
from django.test import TestCase
from .views import home_page
from django.urls import resolve

# from .models import Item
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

    def test_uses_home_template(self):
        resp = self.client.get('/')
        self.assertTemplateUsed(resp, 'home.html')

    # def test_can_save_POST_request(self):
    #     resp = self.client.post('/', data={'item_text': 'A new list item'})
    #     self.assertIn('A new list item', resp.content.decode())
        

# class ItemModelTest(TestCase):
#     def test_saving_and_retrieving_items(self):
#         first_item = Item()
#         first_item.text = 'The first list item'
#         first_item.save()

#         second_item = Item()
#         second_item.text = 'The second list item'
#         second_item.save()

#         saved_items = Item.objects.all()
#         self.assertEqual(saved_items.count(), 2)

#         first_saved_item = saved_items[0]
#         second_saved_item = saved_items[1]
#         self.assertEqual(first_saved_item, 'The first list item')
#         self.assertEqual(second_saved_item, 'The second list item')