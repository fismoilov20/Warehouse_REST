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
        fields = ['id', 'username', 'password', 'is_superuser', 'is_staff']
    
    def create(self, validated_data):
        user = User(
            # email=validated_data['email'],
            username=validated_data['username'],
            is_superuser=validated_data['is_superuser'],
            is_staff=validated_data['is_staff'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

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

