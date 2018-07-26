import unittest
from src import Cleaner


class TestRemoveResources(unittest.TestCase):

    def setUp(self):
        self.cleaner = Cleaner()

    def test_remove_file_link_normal(self):
        text = '[[File:Portrait of Milton Friedman.jpg|right|thumb|upright|[[米爾頓·傅利曼]]是芝加哥學派最知名的經濟學家。]]'
        expected = ''
        actual = self.cleaner._remove_file_links(text)
        self.assertEqual(expected, actual)

        text = ']]\n[[File:Nicaea icon.jpg|thumb|230px|羅馬帝國的[[政教合一]]]]\n[['
        expected = ']]\n\n[['
        actual = self.cleaner._remove_file_links(text)
        self.assertEqual(expected, actual)

    def test_remove_file_link_unfinished(self):
        text = '[[File:Diagram of sentence.png|thumb|科刑流程圖]'
        expected = '[[File:Diagram of sentence.png|thumb|科刑流程圖]'
        actual = self.cleaner._remove_file_links(text)
        self.assertEqual(expected, actual)

    def test_remove_file_link_not_exist(self):
        text = '[File:Emile Durkheim.jpg|thumb|180px|[[爱米尔·涂尔干]]]'
        expected = '[File:Emile Durkheim.jpg|thumb|180px|[[爱米尔·涂尔干]]]'
        actual = self.cleaner._remove_file_links(text)
        self.assertEqual(expected, actual)

    def test_remove_image_link_normal(self):
        text = '[[Image:Transistorer (croped).jpg|thumb|upright|幾個不同大小的電晶體]]'
        expected = ''
        actual = self.cleaner._remove_image_links(text)
        self.assertEqual(expected, actual)
