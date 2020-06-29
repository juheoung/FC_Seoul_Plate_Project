from django.test import TestCase
from model_bakery import baker
from munch import Munch
from rest_framework import status
from rest_framework.test import APITestCase

from blogs.models import Blog


class BlogTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = baker.make('auth.User', _quantity=3)
        self.blogs = []

        for user in self.user:
            self.blogs += baker.make('blogs.Blog', _quantity=3, post_title='1', post_contents='1', post_owner=user)

        self.user = self.user[0]
        self.blog = Blog.objects.filter(post_owner=self.user.id).first()

    def test_post_create(self):
        """"포스트 생성"""
        data = {
            'post_title': 'asdasdad',
            'post_contents': 'sdsadas',
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.post('/api/blogs/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        blog_response = Munch(response.data)
        self.assertTrue(blog_response.id)
        self.assertEqual(blog_response.post_contents, data['post_contents'])
        self.assertEqual(blog_response.post_owner, self.user.id)

    def test_post_list(self):
        """"포스트 리스트"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/blogs/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for blog_response, blog in zip(response.data['results'], self.blogs[::-1]):
            self.assertEqual(blog_response['post_contents'], blog.post_contents)
            self.assertEqual(blog_response['post_owner'], blog.post_owner_id)

    def test_post_detail(self):
        """"포스트 디테일"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f'/api/blogs/{self.blog.id}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        blog_response = Munch(response.data)
        self.assertTrue(blog_response.id)
        self.assertEqual(blog_response.post_contents, self.blog.post_contents)

    def test_post_update(self):
        """포스트 업데이"""
        prev_content = self.blog.post_contents
        data = {
            'post_title': 'abc',
            'post_contents': 'hello world'
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.patch(f'/api/blogs/{self.blog.id}', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        blog_response = Munch(response.data)
        self.assertEqual(blog_response.post_contents, data['post_contents'])
        self.assertNotEqual(blog_response.post_contents, prev_content)

    def test_post_delete(self):
        """포스트 삭제 """
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/api/blogs/{self.blog.id}')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Blog.objects.filter(pk=self.blog.id).count(), 0)
        # 동일
        self.assertFalse(Blog.objects.filter(pk=self.blog.id).exists())


