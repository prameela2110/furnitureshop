# Generated by Django 5.1.2 on 2024-10-24 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0002_product_db'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Contact', models.IntegerField(blank=True, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
