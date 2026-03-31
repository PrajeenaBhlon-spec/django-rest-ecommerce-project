from urllib import request, response

from django.shortcuts import render 
from django.views.decorators.cache import cache_control
from product.models import Product
from .services import GeminiChatbotClient
from core.settings import GEMINI_API_KEY
import json
from django.http import JsonResponse

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home_page(request):
  return render(request , "Home/home.html")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_home_page(request):
  return render(request , "Home/userHome.html")

def productViewBeforeLogin(request):
  products = Product.objects.all()
  return render(request , 'Home/userProductView.html' , {"products": products})

def render_chatbot(request):
  return render(request , "Home/chatbot.html")

def chatbot_view(request): 
  response = None 
  if request.method == "POST": 
    data = json.loads(request.body)
    user_message = data.get("message")
    response = GeminiChatbotClient(api_key=GEMINI_API_KEY).send_message(user_message) 
    return JsonResponse({ "success": True, "response": response})