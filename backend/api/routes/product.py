from django.urls import path

from ..views import ProductList

product_routes = [path("list", ProductList.as_view())]
