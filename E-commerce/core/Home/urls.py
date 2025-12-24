from django.urls import path , include
from . import views 

urlpatterns = [
  path('product' , include("product.urls"))
]