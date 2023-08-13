#!/usr/bin/python3
"""defines "User" class"""
from models.base_model import BaseModel


class User(BaseModel):
    """represents a User
    attributes:
        email (str): user's email
        password (str): user's password
        first_name (str): user's first name
        last_name (str): user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
