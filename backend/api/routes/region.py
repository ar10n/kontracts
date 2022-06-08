from django.urls import path

from ..views.region import RegionList

region_routes = [path("list", RegionList.as_view())]
