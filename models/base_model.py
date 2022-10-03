#!/usr/bin/python3
""" Base Model module """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ Base Model Class """

    def __init__(self, *args, **kwargs):
        """ Initialize BM Object """

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.updated_at = self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ String representation of BM object """
        return ("[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__))

    def save(self):
        """ Update attribute updated_at """
        self.updated_at = datetime.now()

        models.storage.save()

    def to_dict(self):
        """ Return dictionary representation of object """
        my_dict = self.__dict__.copy()
        if type(my_dict["updated_at"]) is not str:
            my_dict.update({"updated_at": self.updated_at.isoformat()})
        if type(my_dict["created_at"]) is not str:
            my_dict.update({"created_at": self.created_at.isoformat()})

        my_dict.update({"__class__": type(self).__name__})
        return my_dict
