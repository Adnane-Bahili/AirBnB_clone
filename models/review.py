#!/usr/bin/python3
"""class Review"""

import models


class Review(models.BaseModel):
    """Class to represent Reviews"""
    place_id = ""
    user_id = ""
    text = ""
