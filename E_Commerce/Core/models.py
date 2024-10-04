from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from random import randrange

class Contact(models.Model):
    phone = PhoneNumberField('phone')
    email = models.EmailField('email')
    facebook = models.URLField('facebook', blank=True, null=True)
    twitter = models.URLField('twitter', blank=True, null=True)
    linkedin = models.URLField('linkedin', blank=True, null=True)
    dribbble = models.URLField('dribbble', blank=True, null=True)
    google_plus = models.URLField('google_plus', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

    def __str__(self) -> str:
        return 'Contact'

class Carousel(models.Model):
    title1 = models.CharField('title1', max_length=255)
    title2 = models.CharField('title2', max_length=255)
    subtitle = models.CharField('subtitle', max_length=255)
    text = models.TextField('text')
    image = models.ImageField('image', upload_to='siteimages')

    class Meta:
        ordering = ['title1', 'title2']
        verbose_name = 'Carousel'
        verbose_name_plural = 'Carousels'

    def __str__(self) -> str:
        return f'{self.title1}{self.title2}'

class Brands(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    subcategory = models.ManyToManyField(Brands, blank=True, related_name='sub')
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, default=f'Easy Polo Black Edition {randrange(99)}')
    price = models.IntegerField("price", default=randrange(30))
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, related_name='brand', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField()
    def __str__(self) -> str:
        return self.name
    
class Circle(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    img = models.ImageField()

class CustomUser(AbstractUser):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='user_products', null=True)