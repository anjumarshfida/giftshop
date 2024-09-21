from django.db import models

# Create your models here.
class ShopTable(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Shopname= models.CharField(max_length=50,null=True, blank=True)
    Address= models.CharField(max_length=50, null=True, blank=True)
    Emailid=models.CharField(max_length=20, null=True, blank=True)
    Phonenumber=models.BigIntegerField(null=True, blank=True)

class ProductTable(models.Model):

    Name= models.CharField(max_length=30, null=True, blank=True)
    Category= models.CharField(max_length=30, null=True, blank=True)
    Productimages=models.FileField(null=True,blank=True,upload_to='productimages')
    Description= models.CharField(max_length=150, null=True, blank=True)

class Offer(models.Model):
    Productid= models.CharField(max_length=50, null=True, blank=True)
    Image=models.FileField(null=True, blank=True, upload_to='Image')
    Category=models.CharField(max_length=50, null=True, blank=True)
    Description=models.CharField(max_length=150, null=True, blank=True)
    Offervalidity=models.IntegerField(null=True, blank=True)


