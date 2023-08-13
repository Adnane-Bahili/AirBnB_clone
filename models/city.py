#!/usr/bin/python3
"""defines "City" class"""
from models.base_model import BaseModel


class City(BaseModel):
    """represents a city
    attributes:
        state_id (str): state's id
        name (str): city name
    """
    state_id = ""
    name = ""
