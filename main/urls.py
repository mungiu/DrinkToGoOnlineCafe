from django.urls import path

from . import views

urlpatterns = [
    path("order_drink", views.order_drink, name="order_drink"),
    path("edit_drink", views.edit_drink, name="edit_drink")
]
