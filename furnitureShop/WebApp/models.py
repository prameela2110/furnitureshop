from django.db import models


# Create your models here.
class Contact_Db(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Contact = models.IntegerField(null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Description = models.TextField(max_length=100, null=True, blank=True)


class SignUp_Db(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    Confirm_Password = models.CharField(max_length=100, null=True, blank=True)


class Cart_Db(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Product_Name = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Total_Price = models.IntegerField(null=True, blank=True)
    Prod_Image = models.ImageField(upload_to="Cart Images", null=True, blank=True)


class CheckOut_Db(models.Model):
    Country = models.CharField(max_length=100, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Place = models.CharField(max_length=100, null=True, blank=True)
    Address = models.TextField(max_length=500, null=True, blank=True)
    Mobile_Number = models.IntegerField(null=True, blank=True)
    Zip = models.IntegerField(null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    Total_Price = models.IntegerField(null=True, blank=True)
    Messages = models.TextField(max_length=400, null=True, blank=True)
