# Generated by Django 5.1.1 on 2024-09-28 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_remove_category_subcategory_category_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
