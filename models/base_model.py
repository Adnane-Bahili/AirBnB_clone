#!/usr/bin/python3
"""defines "BaseModel" class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """represents the BaseModel"""
    def _init_(self, *args, **kwargs):
        """initializes a new BaseModel
        arguments:
            *args (any): not used
            **kwargs (dict): key/value attribute pairs
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """updates "updated_at" with current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns the dictionary of the BaseModel instance
        includes the key/value pair __class__
        that represents the object's class name
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """returns the "print/str" representation of the BaseModel instance"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)