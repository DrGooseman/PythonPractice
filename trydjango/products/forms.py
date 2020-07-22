from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label="The Title", widget=forms.TextInput(attrs={"placeholder":"Your title"}))
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price"
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(label="The Title")
    description = forms.CharField(required=False, 
    widget=forms.Textarea(
            attrs={
                "rows":20,
                "cols": 120,
                "placeholder": "Your decription..."
            }
        )
    )
    price = forms.DecimalField(initial=5.00)
