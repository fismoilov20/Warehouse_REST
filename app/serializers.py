from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError

from .models import *


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def validate_debt(self, value):
        if value > 500000:
            raise ValidationError('A client cannot have such high debts!')
        return value

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

class WarehouseSerializer(ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Warehouse
        fields = '__all__'

class StatsSerializer(ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

