#!/usr/bin/python3
"""defines "Amenity" class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """represents an amenity
    attribute:
        name (str): amenity name
    """
    name = ""
