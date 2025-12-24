from django.shortcuts import render , redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , viewsets
from .serializers import ProductSerializer
from .models import Product
from .forms import ProductForm
from django.http import JsonResponse

class product_api_view(APIView):
  def get(self , request):
    products = Product.objects.all()
    serializer = ProductSerializer(products , many = True)
    return Response(serializer.data ,  status = status.HTTP_200_OK)

  def post(self, request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

def product_add(request):

  if request.method == "POST":
    form = ProductForm(request.POST , request.FILES)
    if form.is_valid():
      form.save()
      return redirect("product-list")
  
  form = ProductForm()
  return render(request , "product/add_product.html" , {"form":form})
  
    
def product_list(request):
  products = Product.objects.all()
  return render(request, "product/product_list.html", {"products": products})
  