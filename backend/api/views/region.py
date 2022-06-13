from rest_framework import filters, generics, permissions
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.views import APIView

from ..models import Region
from ..serializers import RegionSerializer


class RegionList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        obj = Region.objects.all()
        serializer = RegionSerializer(obj, many=True)
        return Response(serializer.data)


class RegionSearch(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
