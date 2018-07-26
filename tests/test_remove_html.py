import unittest
from src import Cleaner


class TestRemoveEmphasis(unittest.TestCase):

    def setUp(self):
        self.cleaner = Cleaner()

    def test_remove_html(self):
        text = '<text xml:space="preserve">'
        expected = ''
        actual = self.cleaner._remove_htmls(text)
        self.assertEqual(expected, actual)
