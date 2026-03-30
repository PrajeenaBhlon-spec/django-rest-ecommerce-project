from django.urls import path , include
from . import views 

urlpatterns = [
  path('product' , include("product.urls")),
  path('chatbot/', views.chatbot_view, name='chatbot_view'),
  path('chatbot/render/', views.render_chatbot, name='render_chatbot')
]