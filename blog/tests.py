from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import BlogPosts

# Create your tests here.

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
            username = 'testuser',
            email = 'test@gmail.com',
            password = 'secret'
        )

        self.post = BlogPosts.objects.create(
            title = 'Yangi post',
            body = 'Post matni',
            author = self.user
        )

    
    def test_string_reprensentation(self):
        post = BlogPosts(title = 'Post mavzusi')
        self.assertEqual(str(post), post.title)

    
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Yangi post')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Post matni')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/10000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Yangi post')
        self.assertTemplateUsed(response, 'post_detail.html')