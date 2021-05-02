from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import OrderList, Order, Cocktail
from .forms import CreateOrderForm
from main.controller import set_price_before_vat


# Create your views here.
def home(response):
    return render(response, "main/home.html", {})


def order_list(response, list_name):
    ls = OrderList.objects.get(name=list_name)
    return render(response, "main/order_list.html", {"ls": ls})


def create_order(response):
    if response.method == "POST":
        form = CreateOrderForm(response.POST)  # holds all info from our form at the time
        if form.is_valid():  # is_valid() exists because CreateOrderForm inherits fom forms.Form
            new_order = Order()
            new_order.order_list_id = OrderList.objects.get(name=form.cleaned_data["order_list_name"]).id
            new_order.number = form.cleaned_data["number"]
            new_order.complete = form.cleaned_data["complete"]
            new_order.save()
            # redirecting to the order list where the order was added
            # ../ goes one slash backwards from the URL we are currently located in
            return HttpResponseRedirect("../order_list/%s" % form.cleaned_data["order_list_name"])
    else:
        form = CreateOrderForm()
    return render(response, "main/create_order.html", {"form": form})


class CocktailCreateView(CreateView):
    model = Cocktail
    fields = ('order', 'drink', 'size', 'comment')
    success_url = reverse_lazy('/order_list/AL')  # temporarily hardcoded TODO refactor


def view_order(response, list_name, order_number):
    order = OrderList.objects.get(name=list_name).order_set.get(number=order_number)
    ordered_cocktails = order.cocktail_set.all()
    return render(response, "main/view_order.html", {"order": order, "ordered_cocktails": ordered_cocktails})
