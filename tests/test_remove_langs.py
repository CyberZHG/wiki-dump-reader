import unittest
from src import Cleaner


class TestRemoveLangs(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.cleaner = Cleaner()

    def test_remove_langs_normal(self):
        text = "[[印欧语系|西方语言]]中“數學”（{{lang-el|μαθηματικά}}）一詞源自於[[古希臘語]]的{{lang|el|μάθημα}}（{" \
               "{lang|la|máthēma}}），其有“學習”、“學問”、“[[科學]]”，以及另外還有個較狹義且技術性的意思－「數學研究」，" \
               "即使在其語源內。其形容詞{{lang|el|μαθηματικός}}（{{lang|la|mathēmatikós}}），意思為''和學習有關的''或" \
               "''用功的''，亦會被用來指''數學的''。其在[[英语]]中表面上的複數形式，及在[[法语]]中的表面複數形式''{{lang|f" \
               "r|les mathématiques}}''，可溯至[[拉丁文]]的中性複數''{{lang|la|mathematica}}''，由[[西塞罗]]譯自希臘" \
               "文複數{{lang|el|τα μαθηματικά}}（{{lang|la|ta mathēmatiká}}），此一希臘語被[[亚里士多德]]拿來指「[[萬" \
               "物皆數]]」的概念。"
        expected = "[[印欧语系|西方语言]]中“數學”（μαθηματικά）一詞源自於[[古希臘語]]的μάθημα（máthēma），其" \
                   "有“學習”、“學問”、“[[科學]]”，以及另外還有個較狹義且技術性的意思－「數學研究」，即使在其語源內。其形容詞μα" \
                   "θηματικός（mathēmatikós），意思為''和學習有關的''或''用功的''，亦會被用來指''數學的''。其在[[英语]]中" \
                   "表面上的複數形式，及在[[法语]]中的表面複數形式''les mathématiques''，可溯至[[拉丁文]]的中性複數''mathe" \
                   "matica''，由[[西塞罗]]譯自希臘文複數τα μαθηματικά（ta mathēmatiká），此一希臘語被[[亚里士多德]]拿來指" \
                   "「[[萬物皆數]]」的概念。"
        actual = self.cleaner._remove_langs(text)
        self.assertEqual(expected, actual)
