from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title" }))
    email = forms.EmailField()
    description = forms.CharField(required=False, 
                widget=forms.Textarea(attrs={
                    "class": "new-class-name two",
                    "id": "my-id-for-textarea",
                    "rows": 10,
                    "cols": 120
                }))
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title")
        if not "news" in title:
            raise forms.ValidationError("This is not a valid title")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.contains("@"):
            raise forms.ValidationError("Not a valid email")
        return title

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