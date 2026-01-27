# Fichier : api_main.py
from ninja import NinjaAPI
from accounts.api import router as accounts_router

api = NinjaAPI(title="Food Spot API")

# On enregistre l'API des comptes sous le préfixe /auth
api.add_router("/auth/", accounts_router)