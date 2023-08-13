#!/usr/bin/python3
"""Defines the "Place" class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """represents a place
    attributes:
        city_id (str): city's id
        user_id (str): user's id
        name (str): place's name
        description (str): place's description
        number_rooms (int): room count
        number_bathrooms (int): bathroom count
        max_guest (int): guest limit
        price_by_night (int): one night's price
        latitude (float): latitude
        longitude (float): longitude
        amenity_ids (list): amenity ids list
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
