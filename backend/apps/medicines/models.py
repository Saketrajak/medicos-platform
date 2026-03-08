from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Medicine(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    real_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)

    stock = models.IntegerField()

    image = models.ImageField(upload_to="medicines/")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name