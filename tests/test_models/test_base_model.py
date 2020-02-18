#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Unittest for base model module.

This unittest is a collection of possible edge cases
on which this module should not be expected to fail,
and cases on which it is expected to fail.

"""
from models.base_model import BaseModel
from datetime import datetime
import pep8
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    """...

    ...
    ...
    """
    def test_pep8_of_base_model(self):
        """pep8 test.

        This test is designed to make sure the Python code
        is up to the pep8 standard.

        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base_model.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_base_model_id_is_string(self):
        """UUID format testing.

        This test is designed to check if any generated UUID
        is correctly generated and has the propper format.

        """
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_base_model_uuid_good_format(self):
        """...

        ...
        ...
        """
        bm = BaseModel()
        self.assertIsInstance(uuid.UUID(bm.id), uuid.UUID)

    def test_base_model_uuid_wrong_format(self):
        """...

        ...
        ...
        """
        bm = BaseModel()
        bm.id = 'Monty Python'
        warn = 'badly formed hexadecimal UUID string'

        with self.assertRaises(ValueError) as msg:
            uuid.UUID(bm.id)

        self.assertEqual(warn, str(msg.exception))

    def test_base_model_uuid_version(self):
        """...

        ...
        ...
        """
        bm = BaseModel()
        conv_uuid = uuid.UUID(bm.id)

        self.assertEqual(conv_uuid.version, 4)

    def test_base_model_different_uuid(self):
        """...

        ...
        ...
        """
        bm_one = BaseModel()
        bm_two = BaseModel()
        conv_uuid_one = uuid.UUID(bm_one.id)
        conv_uuid_two = uuid.UUID(bm_two.id)

        self.assertNotEqual(conv_uuid_one, conv_uuid_two)

    def test_base_model_created_at_is_datetime(self):
        """Datetime test.

        This test is designed to check if the date and time in which a
        class was created are correctly assigned.

        """
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)

    def test_base_model_updated_at_is_datetime(self):
        """Datetime test.

        This test is designed to check if the date and time in which a
        class is updated are correctly assigned.

        """
        bm = BaseModel()
        self.assertIsInstance(bm.updated_at, datetime)
