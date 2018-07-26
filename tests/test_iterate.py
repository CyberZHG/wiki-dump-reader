import os
import unittest
from src import iterate


class TestIterate(unittest.TestCase):

    def test_iterate(self):
        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'zhwiki-test-pages.xml'
        )
        for _ in iterate(file_path):
            pass
