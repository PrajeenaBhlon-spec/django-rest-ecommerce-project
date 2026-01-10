from django.shortcuts import render , redirect
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomUserSeriaizer , UserLoginSerializer , AdminLoginSerializer
from .utils import generate_otp , send_otp_for_password , send_otp_email

def login_page(request):
  return render(request , "Login/login_page.html")

class VerifyOtpApiView(APIView):
  def post(self, request):
    email = request.session['register-email']
    otp_entered = request.data.get('otp')
    try:
      user = CustomUser.objects.get(email=email)
      if str(user.otp) != str(otp_entered):
        return Response({"message":"Invalid OTP"} , status = status.HTTP_400_BAD_REQUEST)
      
      user.is_verified = True
      user.save()
      return Response({"message":"Verifies successfully"} , status = status.HTTP_201_CREATED)
    
    except CustomUser.DoesNotExist:
      return Response({'message':'Customer with this email donot exist'}, status = status.HTTP_400_BAD_REQUEST)
    

def renderUserLogin(request):
  return render(request , 'Login/user_login.html')

class UserLoginApi(APIView):
  def post(self , request):
    serializer = UserLoginSerializer(data = request.data)
    if serializer.is_valid():
      email = serializer.validated_data['email']
      password = serializer.validated_data['password']
      user = authenticate(request, email=email, password=password)
    
      if user is not None and user.is_active and user.is_verified:
        refresh = RefreshToken.for_user(user)
        return JsonResponse({
          'access': str(refresh.access_token),
          'refresh': str(refresh),
          'role': 'user',
          'email':   user.email
        })
      else:
        return Response({'message': 'Invalid credentials'} , status = status.HTTP_400_BAD_REQUEST)

def renderAdminLogin(request):
  return render(request , "Login/admin_login.html")

class AdminLoginApi(APIView):
  def post(self , request):
    serializer = AdminLoginSerializer(data = request.data)
    if serializer.is_valid():
      email = serializer.validated_data["email"]
      password = serializer.validated_data["password"]
      admin = authenticate(request, email=email, password=password)

      if admin is not None and admin.is_active and admin.is_superuser:
        refresh = RefreshToken.for_user(admin)
        return JsonResponse({
          'access': str(refresh.access_token),
          'refresh': str(refresh),
          'role': 'admin' 
        })
      else:
        return Response({'message': 'Invalid credentials'} , status = status.HTTP_400_BAD_REQUEST)

def UserRegister(request):
  return render(request , 'Login/user_register.html')

def RegisterOtp(request):
  return render(request , 'Login/register_otp.html')

class UserRegisterApiView(APIView):
  def post(self , request):
    serializer = CustomUserSeriaizer(data = request.data)
    email = request.data.get("email")
    if serializer.is_valid():
      user = serializer.save()
      otp = generate_otp()
      user.otp = otp
      user.save()
      send_otp_email(user.email , otp)
      request.session['register-email'] = email
      return Response({"message":"user registered successfully. OTP is sent to you email" , "next":"/otppage/"} , status= status.HTTP_201_CREATED)
    else:
      return Response({"message":"invalid"} , status = status.HTTP_400_BAD_REQUEST)
      
      

class VerifyOtpForPassword(APIView):
  def post(self , request):
    email = request.session['user-email']
    otp_entered = request.data.get("otp")
    try:
      user = CustomUser.objects.get(email = email)
      if str(user.otp) != str(otp_entered):
        return Response({"message":"Invalid OTP"} , status = status.HTTP_400_BAD_REQUEST)
        
      user.is_verified = True
      user.save()
      return Response({"message":"Verification successfull.Password   changed"} , status = status.HTTP_201_CREATED)
    
    except CustomUser.DoesNotExist:
      return Response({"message":"Customer with this email donot exist"} , status = status.HTTP_400_BAD_REQUEST)


def ForgotPassword(request):
  return render(request , "Login/forgot_password.html")

def renderForgotOtpPage(request):
  return render(request , "Login/user_otp.html")

class ForgotPasswordApiView(APIView):
  def post(self , request):
    email = request.data.get('email')
    user = CustomUser.objects.get(email = email)
    password = request.data.get("new_password")
    confirm_password = request.data.get("confirm_password")
    if password != confirm_password:
      return Response({"message":"password donot match"} , status = status.HTTP_400_BAD_REQUEST)
    
    request.session['user-email'] = email
    user.set_password(password)
    otp = generate_otp()
    user.otp = otp
    user.save()
    send_otp_for_password(user.email , user.otp)
    return Response({"message":"OTP is sent to your email. Use this otp to change password"} , status = status.HTTP_201_CREATED)


