from django.db import models


# Create your models here.
class Order(models.Model):
    orderNumber = models.CharField(max_length=200)

    def _str_self(self):
        return self.orderNumber


class Cocktail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    drink = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    vat = models.CharField(max_length=200)
    comment = models.CharField(max_length=500)

    def _str_self(self):
        return self.drink
