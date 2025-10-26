# orders/forms.py
from django import forms
from .models import Order
from products.models import Product

class OrderForm(forms.ModelForm):
    # We use a ModelChoiceField for the product list dropdown
    product = forms.ModelChoiceField(
        queryset=Product.objects.filter(quantity__gt=0),
        help_text="Select a product from the list. Only products in stock are shown."
    )

    class Meta:
        model = Order
        fields = ['user_name', 'email', 'address', 'product', 'product_quantity']
        help_texts = {
            'user_name': 'Your full name.',
            'product_quantity': 'How many units you wish to order.',
        }

    def clean(self):
        """
        Custom validation to check if the requested quantity is available in stock.
        """
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        quantity_requested = cleaned_data.get('product_quantity')

        if product and quantity_requested:
            if product.quantity < quantity_requested:
                # This error will be displayed as a non-field error at the top of the form
                raise forms.ValidationError(
                    f"Sorry, only {product.quantity} units of '{product.name}' are available in stock."
                )
        return cleaned_data