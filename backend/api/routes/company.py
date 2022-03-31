from django.urls import path
from ..views import CompanyList, CompanyCreate, CompanyReadUpdateDelete

company_routes = [
    path("list", CompanyList.as_view()),
    path("create", CompanyCreate.as_view()),
    path("<int:pk>", CompanyReadUpdateDelete.as_view())
]
