from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Get the cleaned data from the form
            product = form.cleaned_data['product']
            quantity_ordered = form.cleaned_data['product_quantity']

            # Update the product's stock
            product.quantity -= quantity_ordered
            product.save()

            order = form.save()
            
            return redirect('order_success')
    else:
        form = OrderForm()

    context = {
        'form': form
    }
    return render(request, 'orders/order_form.html', context)

def order_success(request):
    return render(request, 'orders/order_success.html')