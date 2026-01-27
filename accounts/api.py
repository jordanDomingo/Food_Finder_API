# Fichier : accounts/api.py
from ninja import Router
from .models import User, Seller
from .schemas import RegisterSchema, UpgradeSchema
from django.contrib.auth.hashers import make_password

router = Router()

@router.post("/register")
def register(request, data: RegisterSchema):
    user = User.objects.create(
        email=data.email,
        password=make_password(data.password),
        first_name=data.first_name,
        last_name=data.last_name,
        num_phone=data.num_phone,
        sexe=data.sexe,
        role='client'
    )
    return {"message": "Utilisateur créé", "id": str(user.id)}

@router.post("/become-seller")
def become_seller(request, data: UpgradeSchema):
    user = request.user 
    Seller.objects.create(
        user=user,
        brand_name=data.brand_name,
        siret_ou_id=data.siret_ou_id
    )
    user.role = 'owner'
    user.save()
    return {"message": "Profil vendeur activé"}