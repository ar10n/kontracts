from rest_framework import serializers

from ..models.product import Product
from ..serializers.manufacturer import ManufacturerSerializer


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()

    class Meta:
        model = Product
        fields = "__all__"
