from django.db import models
from .ENUMS import DRINKS, SIZES


class OrderList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "List name: " + self.name


class Order(models.Model):
    order_list = models.ForeignKey(OrderList, on_delete=models.CASCADE)
    number = models.CharField(max_length=200)
    complete = models.BooleanField()

    def __str__(self):
        return ("Order number: " + self.number +
                " Order List: " + self.order_list.name)


class Cocktail(models.Model):
    # Field types implementation
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    drink = models.CharField(max_length=200, choices=DRINKS)
    size = models.CharField(max_length=200, choices=SIZES)
    price = models.Field(max_length=200)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return ("Drink: " + self.drink +
                " Size: " + self.size +
                " Vat %: " + self.vat +
                " Price after taxes: " + self.price +
                " Comment: " + self.comment)
