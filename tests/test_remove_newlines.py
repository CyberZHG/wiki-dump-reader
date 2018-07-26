import unittest
from src import Cleaner


class TestRemoveNewlines(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.cleaner = Cleaner()

    def test_remove_newlines(self):
        text = "{{quote|一個民族是一個由歷史所造成的、穩定的人類社群。它是以共同語言、地域、經濟生活、以及表現於一個共同文化的心理" \
               "機制為基礎的。|Stalin 1994, 20 &lt;sup&gt;3&lt;/sup&gt;}}\n\n有些學者則否認這些客觀特質可以被用來當作定義民族" \
               "的[[充分條件]]，甚至是[[必要條件]]（e.g., Canovan 1996; Gellner 1983; Hobsbawm 1992; Renan 1994）。"
        expected = "{{quote|一個民族是一個由歷史所造成的、穩定的人類社群。它是以共同語言、地域、經濟生活、以及表現於一個共同文化的" \
                   "心理機制為基礎的。|Stalin 1994, 20 &lt;sup&gt;3&lt;/sup&gt;}}\n有些學者則否認這些客觀特質可以被用來當作定" \
                   "義民族的[[充分條件]]，甚至是[[必要條件]]（e.g., Canovan 1996; Gellner 1983; Hobsbawm 1992; Renan 1994）。"
        actual = self.cleaner._remove_continuous_newlines(text)
        self.assertEqual(expected, actual)
