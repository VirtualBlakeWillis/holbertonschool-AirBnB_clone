#!/usr/bin/python3
""" Unit Testing for File Storage """
import unittest
from models.engine.file_storage import FileStorage
import pep8

class TestFileStorage(unittest.TestCase):
    """ Test File Storage Class """

    def test_pep8(self):
        """ Test pep8 of files """
        result = pep8.StyleGuide(quiet=True).check_files(
            ['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Found Errors + Warnings")

    def test_class_docstring(self):
        """ Test docstring of Baase Model and its methods """
        self.assertTrue(len(FileStorage.__doc__) >= 1)
        self.assertTrue(len(BaseModel.all.__doc__) >= 1)
        self.assertTrue(len(BaseModel.new.__doc__) >= 1)
        self.assertTrue(len(BaseModel.save.__doc__) >= 1)
        self.assertTrue(len(BaseModel.reload.__doc__) >= 1)
