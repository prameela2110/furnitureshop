# Generated by Django 5.1.2 on 2024-11-15 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0004_checkout_db'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout_db',
            name='Shipping_amt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='checkout_db',
            name='Subtotal',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]