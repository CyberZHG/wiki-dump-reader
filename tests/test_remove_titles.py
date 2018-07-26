import unittest
from src import Cleaner


class TestRemoveTitles(unittest.TestCase):

    def setUp(self):
        self.cleaner = Cleaner()

    def test_remove_titles(self):
        text = "== 研究 =="
        expected = ' 研究 '
        actual = self.cleaner._remove_titles(text)
        self.assertEqual(expected, actual)

        text = "===馬克思主義意義下的「民族」==="
        expected = '馬克思主義意義下的「民族」'
        actual = self.cleaner._remove_titles(text)
        self.assertEqual(expected, actual)

        text = "====主觀意識來定義===="
        expected = '主觀意識來定義'
        actual = self.cleaner._remove_titles(text)
        self.assertEqual(expected, actual)
