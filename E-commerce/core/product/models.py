from django.db import models
from django.conf import settings

class Product(models.Model):
  product_name = models.CharField(max_length=100)
  product_price = models.IntegerField()
  product_image = models.ImageField(upload_to='products/')
  
  def __str__(self):
    return self.product_name
  
class CustomerCart(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete= models.CASCADE , related_name="cart")
  
  def __str__(self):
    return f"Cart of {self.user}"
  
class CartItem(models.Model):
  cart = models.ForeignKey(
    CustomerCart,
    on_delete=models.CASCADE,
    related_name="items"
  )
  product = models.ForeignKey(
    Product,
    on_delete=models.CASCADE
  )
  quantity = models.PositiveIntegerField(default=1)

  def __str__(self):
    return f"{self.product.product_name} x {self.quantity}"
