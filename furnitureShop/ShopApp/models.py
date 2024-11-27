from django.db import models

# Create your models here.
class Category_Db(models.Model):
    Category_Name = models.CharField(max_length=100,null=True,blank=True)
    Description   = models.TextField(max_length=300,null=True,blank=True)
    Images        = models.ImageField(upload_to="category_images",null=True,blank=True)

class Product_Db(models.Model):
      Product_Category = models.CharField(max_length=100,null=True,blank=True)
      Product_Name     = models.CharField(max_length=100,null=True,blank=True)
      Quality          = models.CharField(max_length=100,null=True,blank=True)
      MRP              = models.IntegerField(null=True,blank=True)
      Description      = models.TextField(max_length=500,null=True,blank=True)
      Orgin            = models.CharField(max_length=100,null=True,blank=True)
      Manufacture      = models.CharField(max_length=100,null=True,blank=True)
      img1             = models.ImageField(upload_to="product_images",null=True,blank=True)
      img2             = models.ImageField(upload_to="product_images",null=True,blank=True)
      img3             = models.ImageField(upload_to="product_images",null=True,blank=True)



