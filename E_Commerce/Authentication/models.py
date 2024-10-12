from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from Core.models import *


class CustomUser(AbstractUser):
    products = models.ManyToManyField(Product, related_name='user_products', through='UserProduct')
    username = models.CharField(_("username"), max_length=150, unique=False, help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only." ))
    email = models.EmailField(_("email address"), blank=False, unique=True)
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

class UserProduct(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    class Meta:
        unique_together = ('user', 'product')
    def __str__(self):
        return f"{self.user.username} - {self.product.name} (Count: {self.count})"