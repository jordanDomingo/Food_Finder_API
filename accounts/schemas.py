# Fichier : accounts/schemas.py
from ninja import Schema
from uuid import UUID
from datetime import datetime

class RegisterSchema(Schema):
    email: str
    password: str
    first_name: str
    last_name: str
    num_phone: str
    sexe: str

class UpgradeSchema(Schema):
    brand_name: str
    siret_ou_id: str