# Generated by Django 5.1.1 on 2024-09-28 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0013_remove_subcategory_cate_remove_prod_cate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
