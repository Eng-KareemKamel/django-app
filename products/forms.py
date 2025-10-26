from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'image']
        help_texts = {
            'name': 'The unique name of the product.',
            'price': 'Price in USD. Cannot be negative.',
            'quantity': 'Available stock quantity.',
        }

    def clean_name(self):
        # Example of a simple custom validation
        name = self.cleaned_data.get('name')
        if len(name) < 4:
            raise forms.ValidationError("Product name must be at least 4 characters long.")
        return name