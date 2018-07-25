import unittest
from src import Cleaner


class TestCleanText(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.cleaner = Cleaner()

    def test_case_1(self):
        text = "[[印欧语系|西方语言]]中“數學”（{{lang-el|μαθηματικά}}）一詞源自於[[古希臘語]]的{{lang|el|μάθημα}}（{" \
               "{lang|la|máthēma}}），其有“學習”、“學問”、“[[科學]]”，以及另外還有個較狹義且技術性的意思－「數學研究」，" \
               "即使在其語源內。其形容詞{{lang|el|μαθηματικός}}（{{lang|la|mathēmatikós}}），意思為''和學習有關的''或" \
               "''用功的''，亦會被用來指''數學的''。其在[[英语]]中表面上的複數形式，及在[[法语]]中的表面複數形式''{{lang|f" \
               "r|les mathématiques}}''，可溯至[[拉丁文]]的中性複數''{{lang|la|mathematica}}''，由[[西塞罗]]譯自希臘" \
               "文複數{{lang|el|τα μαθηματικά}}（{{lang|la|ta mathēmatiká}}），此一希臘語被[[亚里士多德]]拿來指「[[萬" \
               "物皆數]]」的概念。"
        expected = "西方语言中“數學”（μαθηματικά）一詞源自於古希臘語的μάθημα（máthēma），其有“學習”、“學問”、“科" \
                   "學”，以及另外還有個較狹義且技術性的意思－「數學研究」，即使在其語源內。其形容詞μαθηματικός（mathēmatikós），" \
                   "意思為和學習有關的或用功的，亦會被用來指數學的。其在英语中表面上的複數形式，及在法语中的表面複數" \
                   "形式les mathématiques，可溯至拉丁文的中性複數mathematica，由西塞罗譯自希臘文複數τα μαθηματικά（t" \
                   "a mathēmatiká），此一希臘語被亚里士多德拿來指「萬物皆數」的概念。"
        actual = self.cleaner.clean_text(text)
        actual, links = self.cleaner.build_links(actual)
        self.assertEqual(expected, actual)
