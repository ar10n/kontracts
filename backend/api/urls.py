from django.urls import include, path

from .views import (
    ClaimCreate,
    ClaimList,
    ClaimReadUpdateDelete,
    ClientCreate,
    ClientList,
    ClientReadUpdateDelete,
    ClientSearch,
    CompanyList,
    CompanySearch,
    ContractCreate,
    ContractList,
    ContractReadUpdateDelete,
    ManufacturerList,
    ProductList,
    RegionList,
    ShipmentCreate,
    ShipmentList,
    ShipmentReadUpdateDelete,
)

urlpatterns = [
    # auth urls
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    # claim urls
    path("claim/list", ClaimList.as_view()),
    path("claim/create", ClaimCreate.as_view()),
    path("claim/<int:pk>", ClaimReadUpdateDelete.as_view()),
    # client urls
    path("client/list", ClientList.as_view()),
    path("client/create", ClientCreate.as_view()),
    path("client/search", ClientSearch.as_view()),
    path("client/<int:pk>", ClientReadUpdateDelete.as_view()),
    # company urls
    path("company/list", CompanyList.as_view()),
    path("company/search", CompanySearch.as_view()),
    # contract urls
    path("contract/list", ContractList.as_view()),
    path("contract/create", ContractCreate.as_view()),
    path("contract/<int:pk>", ContractReadUpdateDelete.as_view()),
    # manufacturer urls
    path("manufacturer/list", ManufacturerList.as_view()),
    # product urls
    path("product/list", ProductList.as_view()),
    # region urls
    path("region/list", RegionList.as_view()),
    # shipment urls
    path("shipment/list", ShipmentList.as_view()),
    path("shipment/create", ShipmentCreate.as_view()),
    path("shipment/<int:pk>", ShipmentReadUpdateDelete.as_view()),
]
