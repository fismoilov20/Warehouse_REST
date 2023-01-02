from django.shortcuts import render, redirect

from .models import *
from.serializers import *

from rest_framework.permissions import *
from rest_framework.views import APIView, Response, status

# Create your views here.

class ProductsAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        products = Product.objects.filter(warehouse__user=request.user)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(warehouse=Warehouse.objects.get(user=request.user))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk):
        product = Product.objects.get(id=pk)
        if request.user == product.warehouse.user:
            product.delete()
            return Response({"delete_message": "Deleted successfully!"})
        return Response({"error_message": "You don't have permissions!"}, status=status.HTTP_403_FORBIDDEN)

    def put(self, request, pk):
        product = Product.objects.get(id=pk)
        if request.user == product.warehouse.user:
            ser = ProductSerializer(product, data=request.data)
            if ser.is_valid():
                ser.save()
                return Response({"updated_data": ser.data}, status=status.HTTP_202_ACCEPTED)
            return Response({"details": ser.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response({"error_message": "You don't have permissions!"}, status=status.HTTP_403_FORBIDDEN)
    

class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WarehouseAPIView(APIView):
    def get(self, request):
        serializer = WarehouseSerializer(Warehouse.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WarehouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ClientAPIView(APIView):
    def get(self, request):
        serializer = ClientSerializer(Client.objects.all(), many=True)
        return Response(serializer.data)
    
    def post(self, request):
        ser = ClientSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)