from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from . import serializers
from product.models import NewProduct, Category
from rest_framework import permissions


class ProductViewSet (ModelViewSet):
    queryset = NewProduct.objects.all()
# serializer_class = serializers.ProductSerializer
    # способ №1
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # способ №2
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny(),]
        else:
            return [permissions.IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProductListSerializer
        else:
            return serializers.ProductSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAdminUser]