#!/usr/bin/python3
""" Base Model module """
import uuid
import datetime

class BaseModel():
    """ Base Model Class """

    def __init__(self):
        """ Initialize Base Model Object """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        print(self.created_at)