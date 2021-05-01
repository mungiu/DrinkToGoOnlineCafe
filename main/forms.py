from django import forms


class CreateOrder(forms.Form):
    order_list_name = forms.CharField(label="Order List Name", max_length=200)
    number = forms.CharField(label="Order number", max_length=200)
    complete = forms.BooleanField(label="Tick if already completed", required=False)
