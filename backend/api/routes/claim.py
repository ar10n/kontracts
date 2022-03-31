from django.urls import path
from ..views import ClaimList, ClaimCreate, ClaimReadUpdateDelete

claim_routes = [
    path("list", ClaimList.as_view()),
    path("create", ClaimCreate.as_view()),
    path("<int:pk>", ClaimReadUpdateDelete.as_view())
]
