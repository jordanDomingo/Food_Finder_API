from ninja import Schema
from uuid import UUID
from typing import  Optional
from datetime import time
from decimal import Decimal

class CategoryOut(Schema):
    id: int
    label: str
    icon_url: Optional[str]

class SpotIn(Schema):
    name: str
    description: Optional[str] = None
    category_id: int
    address: str
    latitude: float
    longitude: float

class SpotOut(Schema):
    id: UUID
    name: str
    description: Optional[str]
    address: str
    latitude: float
    longitude: float
    is_active: bool
    category: Optional[CategoryOut]
    seller_id: UUID

class CategoryIn(Schema):
    label: str
    icon_url: Optional[str] = None



class MenuItemIn(Schema):
    name: str
    price: Decimal
    description: Optional[str] = None
    image_url: Optional[str] = None # Le vendeur peut mettre un lien vers une photo

class MenuItemOut(Schema):
    id: UUID
    name: str
    price: Decimal
    description: Optional[str] = None
    image_url: Optional[str] = None
    is_available: bool


class OpeningHourIn(Schema):
    day_of_week: int
    open_time: time
    close_time: time

class OpeningHourOut(Schema):
    id: int
    day: int
    opening_time: time
    closing_time: time