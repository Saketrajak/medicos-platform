from django.db import models
from apps.users.models import User
from apps.medicines.models import Medicine


class Order(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('delivered', 'Delivered'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)

    quantity = models.IntegerField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.medicine.name