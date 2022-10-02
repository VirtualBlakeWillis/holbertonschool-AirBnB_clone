#!/usr/bin/python3
""" Base Model module """
import uuid
from datetime import datetime
from .__init__ import storage

class BaseModel():
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
            storage.new(self)

    def __str__(self):
        """ String representation of BM object """
        return ("[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__))

    def save(self):
        """ Update attribute updated_at """
        self.updated_at = datetime.now()
        
        storage.save()
        

    def to_dict(self):
        """ Return dictionary representation of object """
        my_dict = self.__dict__.copy()
        format_and_name = {
            "updated_at": self.updated_at.isoformat(),
            "created_at": self.created_at.isoformat(),
            "__class__": type(self).__name__
        }
        my_dict.update(format_and_name)
        return my_dict
