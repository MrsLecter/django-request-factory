from cgitb import handler
import unittest
from unittest import result
from django.test import TestCase, RequestFactory
from django.test import Client
from unittest.mock import patch
from littleapp.views import getInfo, postInfo
from littleapp.models import Basket

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

def test_with_fixtures(TestCase):
    fixtures = ["basket.json"]

    def test_toGetBasket(self):
        client = Client()
        saved_item = Basket.objects.get(id = 3)
        result = client.get('/basket/goods/3')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(saved_item.id, result.json()['data']['id'])
        self.assertEqual(saved_item.name, result.json()['data']['name'])
        self.assertEqual(saved_item.name, result.json()['data']['category'])
        self.assertEqual(saved_item.name, result.json()['data']['price'])
        self.assertEqual(saved_item.name, result.json()['data']['presence'])

    def test_mixed(self):
        client = Client()
        form_data = {'name': 'test_get_post', 'description': 'test_get+post'}
        result = client.post('/basket/', form_data)
        self.assertEqual(result.status_code, 200)
        item_id = result.json()['added_object']
        result2 = client.get(f'/basket/goods/{item_id}/')
        self.assertEqual(result2.status_code, 200)
        added_name = result2.json()['data']['name']
        self.assertEqual(added_name, form_data['name'])

    def test_add(self):
        client = Client()
        form_data = {'good': 'test_method_post', 'description': 'test_post'}
        result = client.post('/add/', form_data)
        self.assertEqual(result.status_code, 200)
        item = Basket.objects.get(id=result.json()['added_object'])
        self.assertEqual(item.name, form_data['good'])


if __name__ == '__main__':
    unittest.main()