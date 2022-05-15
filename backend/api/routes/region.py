from django.urls import path

from ..views import RegionCreate, RegionList, RegionReadUpdateDelete, RegionSearch

region_routes = [
    path("list", RegionList.as_view()),
    path("create", RegionCreate.as_view()),
    path("search", RegionSearch.as_view()),
    path("<int:pk>", RegionReadUpdateDelete.as_view()),
]
