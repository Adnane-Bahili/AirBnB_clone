#!/usr/bin/python3
"""class User from BaseModel"""

import models


class User(models.BaseModel):
    """User representation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
