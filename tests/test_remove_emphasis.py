import unittest
from src import Cleaner


class TestRemoveEmphasis(unittest.TestCase):

    def setUp(self):
        self.cleaner = Cleaner()

    def test_remove_emphasis_bold(self):
        text = "'''游戏工具编程'''是指采用各种开发工具进行开发修改[[电脑]]、[[电视]][[游戏]]的过程。主要的开发工具有以下几大类"
        expected = '游戏工具编程是指采用各种开发工具进行开发修改[[电脑]]、[[电视]][[游戏]]的过程。主要的开发工具有以下几大类'
        actual = self.cleaner._remove_emphasis(text)
        self.assertEqual(expected, actual)

    def test_remove_emphasis_italic(self):
        text = "'''臺灣藍鵲'''（[[學名]]：''{{lang|la|Urocissa caerulea}}''），又稱'''臺灣暗藍鵲'''、'''紅嘴山鵲'''、" \
               "'''長尾山娘'''（[[臺灣閩南語羅馬字拼音方案|閩南語]]：{{Unicode|Tn̂g-bué Suann-niû}}）或'''長尾陣仔'''，為臺" \
               "灣特有種鳥類。臺灣從[[臺灣清治時期|清領時期]]開始就有文獻紀載臺灣藍鵲的資料。1862年，鳥畫家[[约翰·古尔德]]根據英" \
               "國博物學家[[郇和]]寄來的臺灣鳥類標本發表了一篇文章，命名並詳述16種新發現的台灣品種，其中就包含臺灣藍鵲。"
        expected = '臺灣藍鵲（[[學名]]：{{lang|la|Urocissa caerulea}}），又稱臺灣暗藍鵲、紅嘴山鵲、長尾山娘（[[臺灣閩南語羅馬' \
                   '字拼音方案|閩南語]]：{{Unicode|Tn̂g-bué Suann-niû}}）或長尾陣仔，為臺灣特有種鳥類。臺灣從[[臺灣清治時期|清' \
                   '領時期]]開始就有文獻紀載臺灣藍鵲的資料。1862年，鳥畫家[[约翰·古尔德]]根據英國博物學家[[郇和]]寄來的臺灣鳥類' \
                   '標本發表了一篇文章，命名並詳述16種新發現的台灣品種，其中就包含臺灣藍鵲。'
        actual = self.cleaner._remove_emphasis(text)
        self.assertEqual(expected, actual)
