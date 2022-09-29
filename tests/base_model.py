#!/usr/bin/python3
""" Unit Testing for Base Model """
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test Base Model Class """

    def test_str(self):
        my_b = BaseModel()
        d1 = my_b.to_dict()
        self.assertEqual(d1["created_at"], d1["updated_at"])
        my_b.save()
        d1 = my_b.to_dict()
        self.assertNotEqual(d1["created_at"], d1["updated_at"])

if __name__ == "__main__":
    unittest.main()
