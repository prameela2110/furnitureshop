# Generated by Django 5.1.2 on 2024-11-15 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0005_checkout_db_shipping_amt_checkout_db_subtotal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout_db',
            name='Shipping_amt',
        ),
        migrations.RemoveField(
            model_name='checkout_db',
            name='Subtotal',
        ),
        migrations.AddField(
            model_name='checkout_db',
            name='State',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
