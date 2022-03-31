from rest_framework import serializers

from ..models.claim import Claim


class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = "__all__"
