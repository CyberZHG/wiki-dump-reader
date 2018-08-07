import unittest
from wiki_dump_reader import Cleaner


class TestRemoveChoices(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.cleaner = Cleaner()

    def test_remove_choice(self):
        text = "例如，[[全球資訊網]]是在[[歐洲核子研究組織]]由-{A|zh:[[蒂姆·伯纳斯-李]];zh-cn:[[蒂姆·伯纳斯-李]];zh-tw:[[提" \
               "姆·柏納-李]];zh-hk:[[添·柏納-李]];}-創始與發展成功的，原先設計目标為向組織內部和全世界的物理學者提供資訊傳播服務。" \
               "廣受歡迎的[[arXiv]]網站也是在類似狀況下創立的。"
        expected = "例如，[[全球資訊網]]是在[[歐洲核子研究組織]]由[[蒂姆·伯纳斯-李]]創始與發展成功的，原先設計目标為向組織內部和全" \
                   "世界的物理學者提供資訊傳播服務。廣受歡迎的[[arXiv]]網站也是在類似狀況下創立的。"
        actual = self.cleaner._remove_choices(text)
        self.assertEqual(expected, actual)

        text = "廣州非常國會取消軍政府，改總裁-{制}-為總統制"
        expected = "廣州非常國會取消軍政府，改總裁制為總統制"
        actual = self.cleaner._remove_choices(text)
        self.assertEqual(expected, actual)

        text = "一种-{zh-tw:[[自由軟體]];zh-hk:[[自由軟件]];zh-cn:[[自由软件]]}-計劃"
        expected = "一种[[自由軟件]]計劃"
        actual = self.cleaner._remove_choices(text)
        self.assertEqual(expected, actual)

        text = "一种-{zh-tw:[[自由軟體]]}-計劃"
        expected = "一种[[自由軟體]]計劃"
        actual = self.cleaner._remove_choices(text)
        self.assertEqual(expected, actual)
