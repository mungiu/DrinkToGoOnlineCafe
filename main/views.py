from django.db.models import Sum
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .ENUMS import VAT
from .controller import get_price_with_vat
from .models import OrderList, Order, Cocktail, Drink
from .forms import CreateOrderForm, CreateCocktailForm, CreateOrderListForm


# Create your views here.
def home(response):
    order_lists = OrderList.objects.all()
    return render(response, "main/home.html", {"order_lists": order_lists})


def order_list(response, list_name):
    ls = OrderList.objects.get(name=list_name)
    return render(response, "main/order_list.html", {"ls": ls})


def create_order_list(response):
    if response.method == "POST":
        form = CreateOrderListForm(response.POST)
        if form.is_valid():
            new_order_list = OrderList()
            new_order_list.name = form.cleaned_data["name"]
            new_order_list.save()
            return HttpResponseRedirect("../")
    else:
        form = CreateOrderListForm()
    return render(response, "main/create_order_list.html", {"form": form})


def create_order(response):
    if response.method == "POST":
        form = CreateOrderForm(response.POST)  # holds all info from our form at the time
        if form.is_valid():  # is_valid() exists because CreateOrderForm inherits fom forms.Form
            new_order = Order()
            new_order.order_list = OrderList.objects.get(
                name=form.cleaned_data["order_list"].name)
            new_order.number = form.cleaned_data["number"]
            new_order.complete = form.cleaned_data["complete"]
            new_order.save()
            # redirecting to the order list where the order was added
            # ../ goes one slash backwards from the URL we are currently located in
            return HttpResponseRedirect(
                "../order_list/%s" % OrderList.objects.get(name=form.cleaned_data["order_list"].name).name)
    else:
        form = CreateOrderForm()
    return render(response, "main/create_order.html", {"form": form})


def create_cocktail(response):
    if response.method == "POST":
        form = CreateCocktailForm(response.POST)  # holds all info from our form at the time
        if form.is_valid():  # is_valid() exists because CreateOrderForm inherits fom forms.Form
            new_cocktail = Cocktail()
            new_cocktail.order = Order.objects.get(
                id=form.cleaned_data["order"].id,
                number=form.cleaned_data["order"].number,
                complete=form.cleaned_data["order"].complete)
            new_cocktail.drink = Drink.objects.get(
                name=form.cleaned_data["drink"].name,
                price=form.cleaned_data["drink"].price,
                size=form.cleaned_data["drink"].size,
                vat=form.cleaned_data["drink"].vat)
            new_cocktail.comment = form.cleaned_data["comment"]
            new_cocktail.save()
            return HttpResponseRedirect("../view_order/%s/%s"
                                        % (Order.objects.get(number=form.cleaned_data["order"].number).order_list.name,
                                           Order.objects.get(number=form.cleaned_data["order"].number).number))
    else:
        form = CreateCocktailForm()
    return render(response, "main/create_cocktail.html", {"form": form})


def view_order(response, list_name, order_number):
    order = OrderList.objects.get(name=list_name).order_set.get(number=order_number)
    ordered_cocktails = order.cocktail_set.all()
    # order full price after VAT
    order_full_price = Cocktail.objects.filter(order=order).aggregate(
        sum=get_price_with_vat(Sum("drink__price"), VAT))
    return render(response, "main/view_order.html", {"order": order,
                                                     "ordered_cocktails": ordered_cocktails,
                                                     "order_full_price": order_full_price})
