from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("order_list/<str:list_name>", views.order_list, name="order_list"),
    path("create_order_list/", views.create_order_list, name="create_order_list"),
    path("create_order/", views.create_order, name="create_order"),
    path("create_cocktail/", views.create_cocktail, name="create_cocktail"),
    path("view_order/<str:list_name>/<int:order_number>", views.view_order, name="view_order")
]
