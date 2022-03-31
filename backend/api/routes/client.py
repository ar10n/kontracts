from django.urls import path
from ..views import ClientList, ClientCreate, ClientReadUpdateDelete

client_routes = [
    path("list", ClientList.as_view()),
    path("create", ClientCreate.as_view()),
    path("<int:pk>", ClientReadUpdateDelete.as_view())
]
