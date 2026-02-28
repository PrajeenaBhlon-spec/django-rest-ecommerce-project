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
  path('productedit/api/<int:id>/' , views.ProductEditApi.as_view() , name="product-edit-api"),
  path('addtocart/api/<int:id>/' , views.CartApiView.as_view() , name="add-to-cart"),
  path('cartdisplay/api/' , views.UserCartDisplayApi.as_view() , name="cart-display"),
  path('cart/' , views.render_cart_page , name="view-cart"),
  path('productdisplay/' , views.productViewBeforeLogin ),
  path('deletecart/api/<int:id>/' , views.DeleteCartItemApi.as_view() , name="delete-cart-item"),
  path('address/api/' , views.UserAddressApi.as_view() , name='user-address-entry'),
  path('addresspage/' , views.addressPageRender.as_view() , name="address-render"),
  path('payment/' , views.paymentPageRender),
  path('address/' , views.addressFormRender),
  path('deleteone/api/<int:id>/' , views.DeleteOneCartItemApi.as_view()),
  path('addone/api/<int:id>/' , views.AddOneCartItemApi.as_view())
]
