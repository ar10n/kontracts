from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.views import APIView

from ..models import Manufacturer
from ..serializers import ManufacturerSerializer


class ManufacturerList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        obj = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(obj, many=True)
        return Response(serializer.data)
