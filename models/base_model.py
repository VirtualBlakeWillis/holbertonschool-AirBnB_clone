#!/usr/bin/python3
""" Base Model module """
import uuid


class BaseModel():
    """ Base Model Class """

    def __init__(self):
        """ Initialize Base Model Object """

        self.id = str(uuid.uuid4())

