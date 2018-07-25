import unittest
from src import Cleaner


class TestBuildLinks(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.cleaner = Cleaner()

    def test_build_links(self):
        text = "[[印欧语系|西方语言]]中“數學”（μαθηματικά）一詞源自於[[古希臘語]]的μάθημα（máthēma），其" \
                   "有“學習”、“學問”、“[[科學]]”，以及另外還有個較狹義且技術性的意思－「數學研究」，即使在其語源內。其形容詞μα" \
                   "θηματικός（mathēmatikós），意思為''和學習有關的''或''用功的''，亦會被用來指''數學的''。其在[[英语]]中" \
                   "表面上的複數形式，及在[[法语]]中的表面複數形式''les mathématiques''，可溯至[[拉丁文]]的中性複數''mathe" \
                   "matica''，由[[西塞罗]]譯自希臘文複數τα μαθηματικά（ta mathēmatiká），此一希臘語被[[亚里士多德]]拿來指" \
                   "「[[萬物皆數]]」的概念。"
        expected = "西方语言中“數學”（μαθηματικά）一詞源自於古希臘語的μάθημα（máthēma），其有“學習”、“學問”、“科" \
                   "學”，以及另外還有個較狹義且技術性的意思－「數學研究」，即使在其語源內。其形容詞μαθηματικός（mathēmatikós），" \
                   "意思為''和學習有關的''或''用功的''，亦會被用來指''數學的''。其在英语中表面上的複數形式，及在法语中的表面複數" \
                   "形式''les mathématiques''，可溯至拉丁文的中性複數''mathematica''，由西塞罗譯自希臘文複數τα μαθηματικά（t" \
                   "a mathēmatiká），此一希臘語被亚里士多德拿來指「萬物皆數」的概念。"
        actual, links = self.cleaner.build_links(text)
        self.assertEqual(expected, actual)

    def test_no_links(self):
        text = "西方语言中“數學”（μαθηματικά）一詞源自於古希臘語的μάθημα（máthēma），其有“學習”、“學問”、“科" \
                   "學”，以及另外還有個較狹義且技術性的意思－「數學研究」，即使在其語源內。其形容詞μαθηματικός（mathēmatikós），" \
                   "意思為''和學習有關的''或''用功的''，亦會被用來指''數學的''。其在英语中表面上的複數形式，及在法语中的表面複數" \
                   "形式''les mathématiques''，可溯至拉丁文的中性複數''mathematica''，由西塞罗譯自希臘文複數τα μαθηματικά（t" \
                   "a mathēmatiká），此一希臘語被亚里士多德拿來指「萬物皆數」的概念。"
        expected = "西方语言中“數學”（μαθηματικά）一詞源自於古希臘語的μάθημα（máthēma），其有“學習”、“學問”、“科" \
                   "學”，以及另外還有個較狹義且技術性的意思－「數學研究」，即使在其語源內。其形容詞μαθηματικός（mathēmatikós），" \
                   "意思為''和學習有關的''或''用功的''，亦會被用來指''數學的''。其在英语中表面上的複數形式，及在法语中的表面複數" \
                   "形式''les mathématiques''，可溯至拉丁文的中性複數''mathematica''，由西塞罗譯自希臘文複數τα μαθηματικά（t" \
                   "a mathēmatiká），此一希臘語被亚里士多德拿來指「萬物皆數」的概念。"
        text, links = self.cleaner.build_links(text)
        actual, links = self.cleaner.build_links(text)
        self.assertEqual(expected, actual)
        self.assertEqual(id(actual), id(text))

    def test_category(self):
        text = "2004年6月28日 [[User:Shizhao|Shizhao]] [[MediaWiki:Categoryarticlecount]]被保护"
        expected = "2004年6月28日 Shizhao Categoryarticlecount被保护"
        text, links = self.cleaner.build_links(text)
        actual, links = self.cleaner.build_links(text)
        self.assertEqual(expected, actual)

        text = "[[Category:未被普遍承認的歷史國家]]"
        expected = "未被普遍承認的歷史國家"
        text, links = self.cleaner.build_links(text)
        actual, links = self.cleaner.build_links(text)
        self.assertEqual(expected, actual)

        text = "柏拉圖的著作（其中大多數都是對話錄）曾經被以好幾種不同方式出版過；因此對於柏拉圖著作的命名和引用也有數種不同的" \
               "方式。有獨立條目的柏拉圖對話錄介紹可以在[[:Category:柏拉圖對話錄]]找到。"
        expected = "柏拉圖的著作（其中大多數都是對話錄）曾經被以好幾種不同方式出版過；因此對於柏拉圖著作的命名和引用也有數種不同" \
                   "的方式。有獨立條目的柏拉圖對話錄介紹可以在柏拉圖對話錄找到。"
        text, links = self.cleaner.build_links(text)
        actual, links = self.cleaner.build_links(text)
        self.assertEqual(expected, actual)
