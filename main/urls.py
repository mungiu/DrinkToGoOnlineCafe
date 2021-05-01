from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("order_list/<str:list_name>", views.order_list, name="order_list"),
    path("create_order/", views.create_order, name="create_order"),
    path("edit_order/<str:list_name>/<int:order_number>", views.edit_order, name="edit_order")
]
