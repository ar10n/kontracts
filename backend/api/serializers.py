from rest_framework import serializers

from .models import (
    Claim,
    Client,
    Company,
    Contract,
    Manufacturer,
    Product,
    Region,
    Shipment,
)


class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()

    class Meta:
        model = Product
        fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = "__all__"


class ContractSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    company = CompanySerializer()
    region = RegionSerializer()
    products = ProductSerializer(many=True)

    claims = ClaimSerializer(many=True)
    shipments = ShipmentSerializer(many=True)

    class Meta:
        model = Contract
        fields = "__all__"


class ContractCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"
