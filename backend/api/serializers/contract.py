from rest_framework import serializers

from ..models.contract import Contract
from ..serializers.claim import ClaimSerializer
from ..serializers.client import ClientSerializer
from ..serializers.company import CompanySerializer
from ..serializers.product import ProductSerializer
from ..serializers.region import RegionSerializer


class ContractSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    company = CompanySerializer()
    region = RegionSerializer()
    products = ProductSerializer(many=True)

    claims = ClaimSerializer(many=True)

    class Meta:
        model = Contract
        fields = "__all__"


class ContractCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"
