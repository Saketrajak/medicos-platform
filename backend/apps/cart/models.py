from django.db import models
from apps.users.models import User
from apps.medicines.models import Medicine


class Cart(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class CartItem(models.Model):

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.medicine.name