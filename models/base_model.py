#!/usr/bin/python3
""" Base Model module """
import uuid
from datetime import datetime


class BaseModel():
    """ Base Model Class """

    def __init__(self, *args, **kwargs):
        """ Initialize BM Object """
        if kwargs:
            form = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key is not "__class__":
                    self.__dict__.update({key: value})
                if key in ["created_at", "updated_at"]:
                    self.__dict__.update({key: datetime.strptime(value, form)})

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def str_to_dt_obj(self, sr):
        print(" year = " + sr[0:4])
        print(" month = " + sr[5:6])
        print(" day = " + sr[7:8])

    def __str__(self):
        """ String representation of BM object """
        return ("[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__))

    def save(self):
        """ Update attribute updated_at """
        self.updated_at = datetime.now()

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
