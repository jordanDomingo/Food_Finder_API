import uuid
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

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
    


class OpeningHour(models.Model):
    # Ton image utilise un SERIAL (auto-incrément) pour l'ID, Django le fait par défaut
    spot = models.ForeignKey('Spot', on_delete=models.CASCADE, related_name='opening_hours', db_column='spot_id')
    day_of_week = models.SmallIntegerField() # 0 (Dimanche) à 6 (Samedi)
    open_time = models.TimeField()
    close_time = models.TimeField()

    class Meta:
        db_table = 'opening_hours' # Pour forcer le nom de la table si besoin
        unique_together = ('spot', 'day_of_week') # Un stand ne peut avoir qu'un horaire par jour



class MenuItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    spot = models.ForeignKey('Spot', on_delete=models.CASCADE, related_name='menu_items', db_column='spot_id')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True) # Ajout de l'image
    is_available = models.BooleanField(default=True)

    class Meta:
        db_table = 'menu_items'