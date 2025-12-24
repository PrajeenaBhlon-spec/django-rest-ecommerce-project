from .models import CustomUser
from rest_framework import serializers


class CustomUserSeriaizer(serializers.ModelSerializer):
  confirm_password = serializers.CharField()
  class Meta:
    model = CustomUser
    fields = ["username" , "email" , "password" , "confirm_password"]

  def validate(self, data):
    if data["password"] != data["confirm_password"]:
      raise serializers.ValidationError("Passwords do not match")
    return data
  
  def create(self ,validated_data):
    validated_data.pop("confirm_password")
    return CustomUser.objects.create_user(**validated_data)
  
class UserLoginSerializer(serializers.Serializer):
  email = serializers.EmailField()
  password = serializers.CharField()

class AdminLoginSerializer(serializers.Serializer):
  email = serializers.EmailField()
  password = serializers.CharField()