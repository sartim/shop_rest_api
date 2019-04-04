from rest_framework import serializers

from accounts.serializers import UserSerializer
from api.serializers import ProductSerializer
from order.models import Order, OrderItem


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    order_total = serializers.CharField()
    created = serializers.CharField()
    updated = serializers.CharField()
    is_site_order = serializers.CharField()
    is_app_order = serializers.CharField()

    class Meta:
        model = Order
        fields = ('id', 'user', 'order_total', 'created', 'updated', 'is_site_order', 'is_app_order',)
        # fields = '__all__'


class OrderItemSerializer(serializers.Serializer):
    order = OrderSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    price = serializers.CharField()
    quantity = serializers.CharField()

    class Meta:
        model = OrderItem
        fields = ('order', 'product', 'price', 'quantity',)
        # fields = '__all__'
