from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("order_list/<str:name>", views.order_list, name="order_list"),
    path("order_cocktail", views.order_cocktail, name="order_cocktail"),
    # the "cocktail_id" will be passed to the function views.edit_drink
    path("edit_order/<int:order_id>", views.edit_order, name="edit_order")
]
