from django.urls import path
from ..views import ProductList, ProductCreate, ProductReadUpdateDelete

product_routes = [
    path("list", ProductList.as_view()),
    path("create", ProductCreate.as_view()),
    path("<int:pk>", ProductReadUpdateDelete.as_view())
]
