from django.db import models

from main.controller import get_price_with_vat


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
                " Order list name: " + self.order_list.name)


class Drink(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(max_length=200)
    size = models.CharField(max_length=200)
    vat = models.FloatField(max_length=200)

    def __str__(self):
        return ("Name: " + self.name +
                " - Price: " + str(self.price) +
                " - Size: " + self.size +
                " - VAT in %: " + str(self.vat) +
                " - Price with VAT: {:.2f}".format(get_price_with_vat(self.price, self.vat)))


class Cocktail(models.Model):
    # Field types implementation
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return ("Drink: " + str(self.drink) +
                " Comment: " + self.comment)
