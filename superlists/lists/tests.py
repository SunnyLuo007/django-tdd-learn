from django.test import TestCase
from lists.models import Item


# Create your tests here.
class HomePageTest(TestCase):

    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        # content = response.content.decode(encoding='utf8')
        # self.assertIn('To-Do', content)
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_post_request(self):
        self.client.post('/', data={'item_text': 'A new list item'})
        response = self.client.get('/')
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        sencond_item = Item()
        sencond_item.text = 'Item the second'
        sencond_item.save()

        saved_items = Item.objects.all()

        self.assertEqual(saved_items.count(), 2)
        first_saved_item = saved_items[0]
        sencond_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(sencond_saved_item.text, 'Item the second')

    def test_can_save_a_Post_request(self):
        _ = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_post(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')
