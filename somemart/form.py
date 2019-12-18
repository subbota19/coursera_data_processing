from django import forms


class Product(forms.Form):
    title = forms.CharField(label="title", max_length=64)
    description = forms.CharField(label="description", max_length=1024)
    price = forms.IntegerField(label="price", min_value=1, max_value=1000000)
