from django import forms
from .models import Laptop, Order

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ['name', 'price', 'store', 'stock']
        labels = {
            'name': 'მოდელი',
            'price': 'ფასი',
            'store': 'მაღაზია',
            'stock': 'რაოდენობა'
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']
        labels = {
            'quantity': 'რაოდენობა',
        }

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label="მოდელით ძებნა")