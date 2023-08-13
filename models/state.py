#!/usr/bin/python3
"""defines "State" class"""
from models.base_model import BaseModel


class State(BaseModel):
    """represents a state
    attribute:
        name (str): state name
    """
    name = ""
