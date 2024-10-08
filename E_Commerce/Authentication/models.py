from django.db import models
from django.contrib.auth.models import AbstractUser
from Core.models import *


class CustomUser(AbstractUser):
    products = models.ManyToManyField(Product, related_name='user_products', through='UserProduct')

class UserProduct(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    class Meta:
        unique_together = ('user', 'product')
    def __str__(self):
        return f"{self.user.username} - {self.product.name} (Count: {self.count})"