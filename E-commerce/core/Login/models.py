from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager


class CustomManager(BaseUserManager):
  def create_superuser(self , username , email , password , **other_fields):
    other_fields.setdefault("is_staff" , True)
    other_fields.setdefault("is_active" , True)
    other_fields.setdefault("is_superuser" , True)

    if other_fields.get("is_staff") is not True:
      raise ValueError("Superuser must have is_staff=True.")
    if other_fields.get("is_superuser") is not True:
      raise ValueError("Superuser must have is_superuser=True.")
    if other_fields.get("is_active") is not True:
      raise ValueError("Superuser must have is_active = True")
    
    return self.create_user( username ,email , password , **other_fields)
  
  
  def create_user(self , username , email , password , **other_fields):
    email = self.normalize_email(email)
    user = self.model( username = username ,email = email , **other_fields)
    user.set_password(password)
    user.is_active = True
    user.save()
    return user

class CustomUser(AbstractBaseUser , PermissionsMixin):
  username = models.CharField(max_length= 100)
  email = models.EmailField(max_length=100 , unique= True)
  city = models.CharField(max_length= 100)
  locality = models.CharField(max_length= 100)
  tole = models.CharField(max_length= 100)
  otp = models.CharField(max_length= 6)
  phone = models.IntegerField(unique=True , blank = True, null = True)
  is_verified = models.BooleanField(default = False)
  is_active = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["username"]

  objects = CustomManager()
  def __str__(self):
    return self.email