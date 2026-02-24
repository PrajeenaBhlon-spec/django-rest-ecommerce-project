from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ["id" ,"product_name" , "product_price" , "product_image"]
  
  def __str__(self):
    return self.product_name
  
class UserAddressSerializer(serializers.Serializer):
  city = serializers.CharField()
  locality = serializers.CharField() 
  tole = serializers.CharField()
  phone = serializers.IntegerField()