from django.urls import path

from ..views import CompanyList, CompanySearch

company_routes = [
    path("list", CompanyList.as_view()),
    path("search", CompanySearch.as_view()),
]
