# Generated by Django 5.1.2 on 2024-10-23 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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