from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def order_drink(response):
    return HttpResponse("<h1>Welcome to Drink to Go Online Cafe!</h1>")


def edit_drink(response):
    return HttpResponse("<h1>Here you should be able to edit your drink!</h1>")
