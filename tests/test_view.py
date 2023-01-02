from unittest import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from app.models import *
from app.serializers import *

class TestUsersView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        return super().setUp()
    
    def test_all_users(self):
        result = self.client.get('/users')
        assert result.status_code == 200
        assert len(result.data) == 4
        assert result.data[0]['username'] == 'admin'
        self.assertTrue( result.data[0]['is_superuser'] )


class TestProductsView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        token = Token.objects.get(user__username="admin")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        return super().setUp()

    def test_get_products(self):
        result = self.client.get('/products')
        assert result.status_code == 200
        # self.assertEqual(len(result.data), 3)

    # def test_post_product(self):
    #     product = {
    #         "id": 2,
    #         "title": "Rokki-Kroki",
    #         "brand": "Krember",
    #         "amount": 20,
    #         "price": 1500000,
    #         "units": "box",
    #         "income_date": "2022-11-25",
    #         "warehouse": 3
    #     }
    #     result = self.client.post('/products', data=product, format="json")
    #     assert result.status_code == 201
    #     assert result.data['id'] is not None
    #     assert result.data['id'] == Product.objects.last().id
    #     assert result.data['brand'] == 'Krember'

    def test_put_product(self):
        product = {
            "id": 2,
            "title": "Rokki-Kroki",
            "brand": "Krember",
            "amount": 10,
            "price": 750000,
            "units": "box",
            "income_date": "2022-11-25",
            "warehouse": 3
        }
        result = self.client.put('/products/4', data=product, format='json')
        self.assertEqual(result.status_code, 202)
        assert result.data['updated_data']['amount'] == 10
        assert result.data['updated_data']['price'] == 750000