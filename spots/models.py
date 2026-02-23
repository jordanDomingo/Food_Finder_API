import uuid
from django.db import models
from django.conf import settings

class Category(models.Model):
    # SERIAL (PK) -> Auto-incrémentation (1, 2, 3...)
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=100)
    icon_url = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.label

class Spot(models.Model):
    # UUID (PK)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # UN SEUL SELLER (FK) - Un stand appartient à un seul vendeur
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='spots'
    )
    
    # UNE SEULE CATEGORY (FK)
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='spots'
    )
    
    name = models.CharField(max_length=150)
    address = models.TextField()
    
    # Coordonnées (Decimal pour la précision GPS sous SQLite)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (par {self.seller.email})"