from django import forms

from main.models import Cocktail, Order, OrderList


class CreateOrderForm(forms.Form):
    order_list_name = forms.ModelChoiceField(label="Order List Name",
                                             queryset=OrderList.objects.all().order_by('name'))
    number = forms.CharField(label="Order number", max_length=200)
    complete = forms.BooleanField(label="Tick if already completed", required=False)


class CreateCocktailForm(forms.ModelForm):
    class Meta:
        model = Cocktail
        fields = ('order', 'drink', 'size', 'comment')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order'].queryset = Order.objects.none()
        self.fields['drink'].queryset = Order.objects.none()
        self.fields['size'].queryset = Order.objects.none()
