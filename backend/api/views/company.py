from django.http import Http404
from rest_framework import filters, generics
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.views import APIView

from ..models import Company
from ..serializers import CompanySerializer


class CompanyList(APIView):
    def get(self, request):
        obj = Company.objects.all()
        serializer = CompanySerializer(obj, many=True)
        return Response(serializer.data)


class CompanySearch(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
