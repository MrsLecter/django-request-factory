from cgitb import handler
import unittest
from django.test import TestCase, RequestFactory
from django.test import Client
from unittest.mock import patch
from littleapp.views import getInfo, postInfo

def db_mock(*args, **kwargs):
    return '"name": "Asus", "category": "laptop"'

def db_post_mock(*args, **kwargs):
    return 201


class test_RequestFactory_endpoints(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.obj = {"item_name": "ASUS ExpertBook B1", "category":"laptop"}

    @patch('website.dataAccess.getAllObject', db_mock)
    def test_endpoint_get(self):
        request = self.factory.get('/get/')
        response = getInfo(request)
        self.assertEqual(response.content.decode('UTF-8'), '"name": "Asus", "category": "laptop"')
        self.assertEqual(response.status_code, 200)

    @patch('website.dataAccess.postToDatabase', db_post_mock)
    def test_endpoint_post(self):
        request = self.factory.post('/get/', format='json')
        response = postInfo(request, self.obj)
        self.assertEqual(response.status_code, 200)


class test_with_client(TestCase):
    def setUp(self):
        self.client = Client(HTTP_USER_AGENT='Mozilla/5.0')
        self.obj = {"item_name": "ASUS ExpertBook B1", "category":"laptop"}

    def test_get(self):
        response = self.client.get('/get/')
        self.assertEqual(response.status_code, 200)

    def test_redirect(self):
        response = self.client.get('/redirect/' , follow=True)
        self.assertEqual(response.redirect_chain, [('/get', 302), ('/get/', 301)])

if __name__ == '__main__':
    unittest.main()