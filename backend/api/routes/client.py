from django.urls import path

from ..views import ClientCreate, ClientList, ClientReadUpdateDelete, ClientSearch

client_routes = [
    path("list", ClientList.as_view()),
    path("create", ClientCreate.as_view()),
    path("search", ClientSearch.as_view()),
    path("<int:pk>", ClientReadUpdateDelete.as_view()),
]
