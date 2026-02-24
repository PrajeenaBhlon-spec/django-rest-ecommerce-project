from django.shortcuts import render 
from django.views.decorators.cache import cache_control
from product.models import Product

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home_page(request):
  return render(request , "Home/home.html")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_home_page(request):
  return render(request , "Home/userHome.html")

def productViewBeforeLogin(request):
  products = Product.objects.all()
  return render(request , 'Home/userProductView.html' , {"products": products})