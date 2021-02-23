from app.models import ProductModel
from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.FloatField()
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        return ProductModel.objects.create(**validated_data)