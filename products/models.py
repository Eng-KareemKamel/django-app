from django.db import models
from django.core.exceptions import ValidationError

def validate_positive(value):
    if value < 0:
        raise ValidationError('This value cannot be negative.')

class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_positive])
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0) # Renamed from qnantity

    def __str__(self):
        return f"{self.name} - In Stock: {self.quantity}"