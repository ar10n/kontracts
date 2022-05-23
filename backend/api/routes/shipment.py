from django.urls import path
from ..views import ShipmentList, ShipmentCreate, ShipmentReadUpdateDelete

shipment_routes = [
    path("list", ShipmentList.as_view()),
    path("create", ShipmentCreate.as_view()),
    path("<int:pk>", ShipmentReadUpdateDelete.as_view())
]
