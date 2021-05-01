from django.db import models


# Create your models here.

class OrderList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "List name: " + self.name


class Order(models.Model):
    order_list = models.ForeignKey(OrderList, on_delete=models.CASCADE)
    number = models.CharField(max_length=200)
    complete = models.BooleanField()

    def __str__(self):
        return "Order number: " + self.number


class Cocktail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    drink = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    vat = models.CharField(max_length=200)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return ("Drink: " + self.drink +
                " Size: " + self.size +
                " Vat %: " + self.vat +
                " Price before taxes: " + self.price +
                " Price after taxes: " + (float(self.price)*(1 + (float(self.vat)/100))) +
                " Comment: " + self.comment)
