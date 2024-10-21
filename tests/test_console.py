import unittest
from console import HBNBCommand
from models import FileStorage

class TestCreate(unittest.TestCase):
        def setUp(Self):
                """Make sure storage is cleared before testing"""
                storage.reload()
        