from unittest import TestCase

from app.serializers import *
from app.models import *

class TestClientSerializer(TestCase):
    def setUp(self) -> None:
        self.data = {
            "id": 5, 
            "name": "Ali", 
            "shop_name": "Coca-Cola",
            "phone": "+998951357846",
            "address": "Fergana, Alisher Navoi",
            "debt": 0,
            "warehouse": Warehouse.objects.get(id=1),
        }
        return super().setUp()
    
    def test_client_ser(self):
        ser = ClientSerializer(self.data)
        assert ser.data["id"] == 5
        assert ser.data["shop_name"] == "Coca-Cola"
        assert ser.data["warehouse"] == 1
        
    def test_validate_debt_valid(self):
        client = {
            "id": 5, 
            "name": "Ali", 
            "shop_name": "Coca-Cola",
            "phone": "+998951357846",
            "address": "Fergana, Alisher Navoi",
            "debt": 0,
            "warehouse": 1,
        }
        ser = ClientSerializer(data=client)
        assert ser.is_valid() == True

    def test_validate_debt_invalid(self):
        client = {
            "id": 5, 
            "name": "Ali", 
            "shop_name": "Coca-Cola",
            "phone": "+998951357846",
            "address": "Fergana, Alisher Navoi",
            "debt": 700000,
            "warehouse": 1,
        }
        ser = ClientSerializer(data=client)
        assert ser.is_valid() == False
        print(ser.errors['debt'])
        assert ser.errors['debt'][0] == 'A client cannot have such high debts!'