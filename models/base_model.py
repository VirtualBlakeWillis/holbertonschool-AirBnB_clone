#!/usr/bin/python3
""" Base Model module """
import uuid


class BaseModel():
    """ Base Model Class """

    def __init__(self):
        """ Initialize Base Model Object """

        self.id = str(uuid.uuid4())

    def __str__(self):
        print("[{}] ({}) {}".format(self.__class__, self.id, to_dict(self)))

    @classmethod
    def to_dict(cls):
        tdn = self.__dict__
        format_time = {
            "updated_at": tdn['updated_at'].strftime("%Y-%m-%dT%H:%M:%S.%f")
            "created_at": tdn['created_at'].strftime("%Y-%m-%dT%H:%M:%S.%f")
        }
        tdn.update("__class__": cls.__name__)
        tdn.update(format_time)
        return tdn
