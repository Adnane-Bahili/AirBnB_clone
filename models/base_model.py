#!/usr/bin/python3
"""Class BaseModel"""

from datetime import datetime
import uuid
import models


class BaseModel:
    """Base Model Class"""
    def __init__(self, *args, **kwargs):
        """__init__ of class Basemodel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        for name, value in kwargs.items():
            """searches dict for keys"""
            if name == "__class__":
                continue
            setattr(self, name, value)
        if "id" not in kwargs:
            models.storage.new(self)

    def __setattr__(self, name, value):
        """Maintain correct types for non-string attributes."""
        if name in ['created_at', 'updated_at']:
            if isinstance(value, str):
                try:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                except ValueError:
                    raise AttributeError("Invalid value: ({}) for name: ({})"
                                         .format(value, name))
        super().__setattr__(name, value)

    def __str__(self):
        """Description of the class class name self.id self.__dict__"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update the public instance update_at with the current_time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary with key and values of instance"""
        d = {}
        d.update(self.__dict__)
        d['created_at'] = d['created_at'].isoformat()
        d['updated_at'] = d['updated_at'].isoformat()
        d['__class__'] = self.__class__.__name__
        return d
