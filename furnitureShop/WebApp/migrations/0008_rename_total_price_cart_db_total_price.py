# Generated by Django 5.1.2 on 2024-11-24 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0007_cart_db_prod_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart_db',
            old_name='TotaL_Price',
            new_name='Total_Price',
        ),
    ]