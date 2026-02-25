from django.shortcuts import render , redirect
from rest_framework.decorators import APIView , permission_classes 
from django.views import View
from rest_framework.response import Response
from rest_framework import status , viewsets
from .serializers import ProductSerializer , UserAddressSerializer
from .models import Product , CustomerCart , CartItem 
from Login.models import CustomUser
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated 

def productViewBeforeLogin(request):
  products = Product.objects.all()
  return render(request , 'Home/userProductView.html' , {"products": products})

def productViewBeforeLogin(request):
  products = Product.objects.all()
  return render(request , 'Home/userProductView.html' , {"products": products})

def renderUserList(request):
  products = Product.objects.all()
  return render(request , 'product/product_list_user.html' , {"products": products})

def renderAdminList(request):
  products = Product.objects.all()
  return render(request , 'product/product_list_admin.html' ,  {"products": products})

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

  def destroy(self, request, pk=None):
    try:
      product = Product.objects.get(pk=pk)
      product.delete()
      return Response({"message": "Product deleted successfully!"}, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
      return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    
  

def product_add(request):
  if request.method == "POST":
    form = ProductForm(request.POST , request.FILES)
    if form.is_valid():
      form.save()
      return redirect("product-list-admin")
  
  form = ProductForm()
  return render(request , "product/add_product.html" , {"form":form})
  


class ProductEditApi(APIView):
  def post(self , request , id):
    price = request.data.get("product_price")
    try:
      product = Product.objects.get(id = id)
      product.product_price = price
      product.save()
      return Response({"message":"Product price changed successfully."} , status = status.HTTP_201_CREATED)
    except Product.DoesNotExist:
      return Response({"message":"product with this id donot exist"}, status = status.HTTP_400_BAD_REQUEST)
    
class CartApiView(APIView):
  permission_classes = [IsAuthenticated]
  authentication_classes = [JWTAuthentication]
  def post(self, request, id):
    cart, created = CustomerCart.objects.get_or_create(user=request.user)
    try:
      product = Product.objects.get(id=id)
    except Product.DoesNotExist:
      return Response({"message": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:
      cart_item.quantity += 1
      cart_item.save()

    return Response({
      "message": "Product added to cart.",
      "product": product.product_name,
      "quantity": cart_item.quantity
    }, status=status.HTTP_200_OK)
  
class UserCartDisplayApi(APIView):
  def get(self, request):
    cart, created = CustomerCart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    data = [
      {
        "id": item.id ,
        "image":item.product.product_image.url,
        "name": item.product.product_name,
        "price": item.product.product_price,
        "quantity": item.quantity,
      }
      for item in items
    ]
    total = sum(item["price"] * item["quantity"] for item in data)
    return Response({"items": data, "total": total})
    

def render_cart_page(request):
  return render(request , "product/user_cart.html")


class DeleteCartItemApi(APIView):
  def delete(self , request , id):
    cart, created = CustomerCart.objects.get_or_create(user=request.user)
    cart_item = CartItem.objects.get(id = id)
    cart_item.delete()
    return Response({"message": "Product deleted successfully!"}, status=status.HTTP_200_OK)
    
class UserAddressApi(APIView):
  permission_classes = [IsAuthenticated]
  def post(self , request):
    user = request.user
    serializer = UserAddressSerializer(data = request.data)
    if serializer.is_valid():
      user.city = serializer.validated_data['city']
      user.locality = serializer.validated_data['locality']
      user.tole = serializer.validated_data['tole']
      user.phone = serializer.validated_data['phone']
      user.save()
      return Response({"message":"succesfull"} , status = status.HTTP_200_OK)
    else:
      return Response({"message":"unsuccessfull"} , status = status.HTTP_400_BAD_REQUEST)

    
      
class addressPageRender(APIView):
  permission_classes = [IsAuthenticated]
  def get(self , request):
    user = request.user
    print(user.city)
    if user.city and user.locality and user.tole and user.phone:
      return Response({'message':'data exists'} , status = status.HTTP_200_OK)
    else:
      return Response({'message':'data donot exists'} , status = status.HTTP_400_BAD_REQUEST)
    
def paymentPageRender(request):
  return render(request , 'product/payment.html')

def addressFormRender(request):
  return render(request , 'product/user_address.html')