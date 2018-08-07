import unittest
from wiki_dump_reader import Cleaner


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

    def test_case_3(self):
        text = "例如，[[全球資訊網]]是在[[歐洲核子研究組織]]由-{A|zh:[[蒂姆·伯纳斯-李]];zh-cn:[[蒂姆·伯纳斯-李]];zh-tw:[[提" \
               "姆·柏納-李]];zh-hk:[[添·柏納-李]];}-創始與發展成功的，原先設計目标為向組織內部和全世界的物理學者提供資訊傳播服務。" \
               "廣受歡迎的[[arXiv]]網站也是在類似狀況下創立的。"
        expected = "例如，全球資訊網是在歐洲核子研究組織由蒂姆·伯纳斯-李創始與發展成功的，原先設計目标為向組織內部和全世界的物理學" \
                   "者提供資訊傳播服務。廣受歡迎的arXiv網站也是在類似狀況下創立的。"
        actual = self.cleaner.clean_text(text)
        actual, links = self.cleaner.build_links(actual)
        self.assertEqual(expected, actual)

    def test_case_4(self):
        text = "亚里士多德死后，整个哲学界陷入了独立时期，称为{{link-en|希腊化哲学|Hellenistic_philosophy}}时期。因为整个社会" \
               "和政治陷入混乱。这段时期产生了[[斯多葛学派]]和[[伊壁鸠鲁学派]]，以及[[皮浪主义|怀疑主义派]]、[[新柏拉图主义|新柏" \
               "拉图派]]和{{le|新毕达哥拉斯主义|Neopythagoreanism}}。这些学派的共同特点是伦理化。斯多葛学派主要是顺应自然和自制" \
               "。伊壁鸠鲁学派则是把快乐作为生活的本质和善的标准。而新柏拉图派和新毕达哥拉斯派都是带有[[宗教]]主义的哲学，并逐渐产" \
               "生融化[[基督教]]和希腊哲学于一体的理论，即为后来的[[基督教哲学]]。"
        expected = "亚里士多德死后，整个哲学界陷入了独立时期，称为希腊化哲学时期。因为整个社会和政治陷入混乱。这段时期产生了斯多葛学" \
                   "派和伊壁鸠鲁学派，以及怀疑主义派、新柏拉图派和新毕达哥拉斯主义。这些学派的共同特点是伦理化。斯多葛学派主要是顺应" \
                   "自然和自制。伊壁鸠鲁学派则是把快乐作为生活的本质和善的标准。而新柏拉图派和新毕达哥拉斯派都是带有宗教主义的哲学，" \
                   "并逐渐产生融化基督教和希腊哲学于一体的理论，即为后来的基督教哲学。"
        actual = self.cleaner.clean_text(text)
        actual, links = self.cleaner.build_links(actual)
        self.assertEqual(expected, actual)
