from django.shortcuts import render
from django.http import HttpResponse
from .models import OrderList, Order, Cocktail


# Create your views here.
def home(response):
    return render(response, "main/home.html", {})


def order_list(response, name):
    ls = OrderList.objects.get(name=name)
    return render(response, "main/order_list.html", {"ls": ls})


def order_cocktail(response):
    return HttpResponse("<h1>Welcome to Drink to Go Online Cafe!</h1>")


def edit_order(response, order_id):
    return HttpResponse("<h1>You are currently editing drink with id: %s</h1>" % order_id)


