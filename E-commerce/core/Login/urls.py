from django.urls import path , include
from . import views 
from Home import views as home_views
from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('' , views.login_page ),

  path('admin/' , views.renderAdminLogin, name="admin-login" ),
  path('api/adminLogin/' , views.AdminLoginApi.as_view() , name="admin-login-api" ),

  path('userlogin/' , views.renderUserLogin , name="user-login"),
  path('api/userlogin/' ,views.UserLoginApi.as_view(), name='user-login-api'),

  path('register/' , views.UserRegister, name="user-register"),
  path('otppage/' , views.RegisterOtp , name="register-otp"),
  path('api/register/' , views.UserRegisterApiView.as_view() , name="user-register-api" ),
  path('api/verifyotp/' , views.VerifyOtpApiView.as_view()  , name = "user-otp-verify"),

  path('userpage/' , home_views.user_home_page , name="user-page"),
  path('adminpage/' , home_views.home_page , name = "admin-page"),
  
  
  path('forgototp/' , views.renderForgotOtpPage , name = "forgot-otp-page"),
  path('forgot/' , views.ForgotPassword , name="forgot-password"),
  path('api/forgot/' , views.ForgotPasswordApiView.as_view() , name='forgot-password-api'),
  path('api/verifyotppassword/' , views.VerifyOtpForPassword.as_view() , name="user-otp-for-password")
]

