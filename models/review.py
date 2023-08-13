#!/usr/bin/python3
"""defines "Review" class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """represents a review
    attributes:
        place_id (str): place's id
        user_id (str): user's id
        text (str): review
    """
    place_id = ""
    user_id = ""
    text = ""
