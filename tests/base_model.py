#!/usr/bin/python3
""" Unit Testing for Base Model """
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ Test Base Model Class """

    def SetUp(self):
        my_b = BaseModel()

    def test_str(self):
        self.assertEqual(my_b.str(), )

if __name__ == "__main__":
    unittest.main()
