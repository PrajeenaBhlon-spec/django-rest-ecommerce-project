from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from . import views

router = DefaultRouter()
router.register('product', ProductViewSet) 

urlpatterns = [
  path('', include(router.urls)),
  path('productlistuser/' , views.renderUserList , name = "product-list-user"),
  path('productlistadmin/' , views.renderAdminList , name="product-list-admin" ),
  path('productadd/' , views.product_add , name="product-add"),
  path('productedit/api/<int:id>/' , views.ProductEditApi.as_view() , name="product-edit-api")
]
