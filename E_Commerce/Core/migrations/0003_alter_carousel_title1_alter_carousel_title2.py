# Generated by Django 5.1.1 on 2024-09-26 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_carousel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='title1',
            field=models.CharField(max_length=255, verbose_name='title1'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='title2',
            field=models.CharField(max_length=255, verbose_name='title2'),
        ),
    ]
