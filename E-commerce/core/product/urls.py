from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from . import views


router = DefaultRouter()
router.register('product', ProductViewSet) 

urlpatterns = [
  path('', include(router.urls)),
  path('productlist/' , views.product_list , name = "product-list"),
  path('productadd/' , views.product_add , name="product-add")
]
