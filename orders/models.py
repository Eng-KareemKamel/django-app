from django.db import models
from products.models import Product

class Order(models.Model):
    user_name = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} for {self.product.name} by {self.user_name}"