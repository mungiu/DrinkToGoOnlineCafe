from django import forms

from main.models import Order, OrderList, Drink


class CreateOrderForm(forms.Form):
    order_list = forms.ModelChoiceField(label="Order List Name", queryset=OrderList.objects.all().order_by('name'))
    number = forms.CharField(label="Order number", max_length=200)
    complete = forms.BooleanField(label="Tick if already completed", required=False)


class CreateCocktailForm(forms.Form):
    order = forms.ModelChoiceField(label="Order number: ", queryset=Order.objects.all().order_by('number'))
    drink = forms.ModelChoiceField(label="Drink name: ", queryset=Drink.objects.all().order_by('name'))
    comment = forms.CharField(label="Comment: ", max_length=200)
