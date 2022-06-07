from django.urls import path

from ..views import ManufacturerList

manufacturer_routes = [path("list", ManufacturerList.as_view())]
