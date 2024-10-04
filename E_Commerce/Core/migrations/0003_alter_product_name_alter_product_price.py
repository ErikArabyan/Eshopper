# Generated by Django 5.1.1 on 2024-10-04 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_alter_customuser_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='Easy Polo Black Edition 5', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=2, verbose_name='price'),
        ),
    ]
