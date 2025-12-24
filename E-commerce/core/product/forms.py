from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = ["id" , "product_name" , "product_price" , "product_image"]