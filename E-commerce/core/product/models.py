from django.db import models

# Create your models here.
class Product(models.Model):
  product_name = models.CharField(max_length=100)
  product_price = models.IntegerField()
  product_image = models.ImageField(upload_to='products/')
  
  def __str__(self):
    return self.product_name