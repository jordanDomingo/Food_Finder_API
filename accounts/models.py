# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    num_phone = models.CharField(max_length=20, unique=True)
    sexe = models.CharField(max_length=1, choices=[('M', 'M'), ('F', 'F'), ('A', 'A')])
    role = models.CharField(max_length=20, default='client')
    created_at = models.DateTimeField(auto_now_add=True)
    
    username = None 
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    brand_name = models.CharField(max_length=150)
    siret_ou_id = models.CharField(max_length=50)