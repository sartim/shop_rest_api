from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # def create(self, validated_data):
    #     pass
    #
    # def update(self, instance, validated_data):
    #     pass

    class Meta:
        model = Product
        fields = ('category', 'name', 'slug', 'image', 'description', 'price', 'stock', 'available', 'created',
                  'updated',)
        # fields = '__all__'
