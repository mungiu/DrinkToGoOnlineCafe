from django.shortcuts import render
from django.http import HttpResponse
from .models import OrderList, Order, Cocktail
from .forms import CreateOrder


# Create your views here.
def home(response):
    return render(response, "main/home.html", {})


def order_list(response, list_name):
    ls = OrderList.objects.get(name=list_name)
    return render(response, "main/order_list.html", {"ls": ls})


def create_order(response):
    if response.method == "POST":
        form = CreateOrder(response.POST)  # holds all info from our form at the time
        if form.is_valid():  # is_valid() exists because CreateOrder inherits fom forms.Form
            new_order = Order()
            new_order.order_list_id = OrderList.objects.get(name=form.cleaned_data["order_list_name"]).id
            new_order.number = form.cleaned_data["number"]
            new_order.complete = form.cleaned_data["complete"]
            new_order.save()
    else:
        form = CreateOrder()
    return render(response, "main/create_order.html", {"form": form})


def edit_order(response, list_name, order_number):
    order = OrderList.objects.get(name=list_name).order_set.get(number=order_number)
    return render(response, "main/edit_order.html", {"order": order})
