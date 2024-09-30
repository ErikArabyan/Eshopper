# Generated by Django 5.1.1 on 2024-09-26 13:54

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='phone')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='twitter')),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='linkedin')),
                ('dribbble', models.URLField(blank=True, null=True, verbose_name='dribbble')),
                ('google_plus', models.URLField(blank=True, null=True, verbose_name='google_plus')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contact',
            },
        ),
    ]
