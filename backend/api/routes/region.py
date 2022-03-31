from django.urls import path
from ..views import RegionList, RegionCreate, RegionReadUpdateDelete

region_routes = [
    path("list", RegionList.as_view()),
    path("create", RegionCreate.as_view()),
    path("<int:pk>", RegionReadUpdateDelete.as_view())
]
