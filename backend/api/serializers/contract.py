from rest_framework import serializers

from ..models.contract import Contract
from ..serializers.client import ClientSerializer
from ..serializers.company import CompanySerializer
from ..serializers.region import RegionSerializer
from ..serializers.product import ProductSerializer


class ContractSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    company = CompanySerializer()
    region = RegionSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Contract
        fields = "__all__"


class ContractCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"
