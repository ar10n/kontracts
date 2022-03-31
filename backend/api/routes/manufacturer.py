from django.urls import path
from ..views import ManufacturerList, ManufacturerCreate, ManufacturerReadUpdateDelete

manufacturer_routes = [
    path("list", ManufacturerList.as_view()),
    path("create", ManufacturerCreate.as_view()),
    path("<int:pk>", ManufacturerReadUpdateDelete.as_view())
]
