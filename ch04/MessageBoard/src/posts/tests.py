from django.test import TestCase

from .models import Post

class PostModelTest(TestCase):
    
    def setUp(self):
        Post.objects.create(text='just a test')

    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')

class HomePageViewTest(TestCase):

    def setUP(self):
        Post.objects.create(text='this is HomeView test')
    
    def test_view_url_exitsts_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reversed('/home/'))
        self.assertEqual(resp.status_code,200)

    def test_view_uses_correct_tempate(self):
        resp = self.client.get(reversed('/home/'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
