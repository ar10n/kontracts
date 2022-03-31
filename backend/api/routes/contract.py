from django.urls import path
from ..views import ContractList, ContractCreate, ContractReadUpdateDelete

contract_routes = [
    path("list", ContractList.as_view()),
    path("create", ContractCreate.as_view()),
    path("<int:pk>", ContractReadUpdateDelete.as_view())
]
