#!/usr/bin/python3
"""defines "FileStorage" class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """represents an abstract storage engine
    attributes:
        path_of_file (str): name of a file to save objects to
        ob_ject (dict): instantiated objects dictionary
    """
    path_of_file = "file.json"
    ob_ject = {}

    def all(self):
        """returns the dictionary ob_ject"""
        return FileStorage.ob_ject

    def new(self, obj):
        """set in ob_ject obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.ob_ject["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """serializes ob_ject to the JSON file path_of_file"""
        odict = FileStorage.ob_ject
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.path_of_file, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """deserializes the JSON file path_of_file to ob_ject,
        when it exists"""
        try:
            with open(FileStorage.path_of_file) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
