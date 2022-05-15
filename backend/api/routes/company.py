from django.urls import path

from ..views import CompanyCreate, CompanyList, CompanyReadUpdateDelete, CompanySearch

company_routes = [
    path("list", CompanyList.as_view()),
    path("create", CompanyCreate.as_view()),
    path("search", CompanySearch.as_view()),
    path("<int:pk>", CompanyReadUpdateDelete.as_view()),
]
