from django.urls import include, path

from .routes import (
    claim_routes,
    client_routes,
    company_routes,
    contract_routes,
    manufacturer_routes,
    product_routes,
    region_routes,
    shipment_routes,
)

urlpatterns = [
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("claim/", include(claim_routes)),
    path("client/", include(client_routes)),
    path("company/", include(company_routes)),
    path("contract/", include(contract_routes)),
    path("manufacturer/", include(manufacturer_routes)),
    path("product/", include(product_routes)),
    path("region/", include(region_routes)),
    path("shipment/", include(shipment_routes)),
]
