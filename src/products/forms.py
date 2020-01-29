from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput)
    description = forms.CharField(required=False, 
                widget=forms.Textarea(attrs={
                    "class": "new-class-name two",
                    "id": "my-id-for-textarea",
                    "rows": 10,
                    "cols": 120
                }))
    price = forms.DecimalField(initial=00.00)