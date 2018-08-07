import unittest
from wiki_dump_reader import Cleaner


class TestRemoveComments(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.cleaner = Cleaner()

    def test_remove_comments_normal(self):
        text = "[[面包]]是德国饮食的重要组成部分。德国出产近600种面包和1,200种糕点和[[圆面包]]。德国[[奶酪]]的生产数量占到全欧" \
               "洲的近三分之一{{refTag|name=IG|1=[https://books.google.com/books?id=sjW9adVFS2kC&amp;pg=PA113 The " \
               "Complete Idiot's Guide to Cheeses of the World - Steve Ehlers, Jeanette Hurt<!-- Bot generated " \
               "title -->]. pp. 113-115.}}。2012年，超过99%在德国生产的肉类为猪肉、鸡肉和牛肉。香肠在德国极为普遍，生产种类" \
               "近1,500种，包括[[德国油煎香肠|油煎香肠]]、[[巴伐利亚白香肠|白香肠]]和[[德國咖哩香腸|咖喱香肠]]等"
        expected = "[[面包]]是德国饮食的重要组成部分。德国出产近600种面包和1,200种糕点和[[圆面包]]。德国[[奶酪]]的生产数量占到" \
                   "全欧洲的近三分之一{{refTag|name=IG|1=[https://books.google.com/books?id=sjW9adVFS2kC&amp;pg=PA113" \
                   " The Complete Idiot's Guide to Cheeses of the World - Steve Ehlers, Jeanette Hurt]. pp. " \
                   "113-115.}}。2012年，超过99%在德国生产的肉类为猪肉、鸡肉和牛肉。香肠在德国极为普遍，生产种类近1,500种，" \
                   "包括[[德国油煎香肠|油煎香肠]]、[[巴伐利亚白香肠|白香肠]]和[[德國咖哩香腸|咖喱香肠]]等"
        actual = self.cleaner._remove_comments(text)
        self.assertEqual(expected, actual)
