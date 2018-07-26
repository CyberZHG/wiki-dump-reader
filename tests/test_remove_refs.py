import unittest
from src import Cleaner


class TestRemoveRefs(unittest.TestCase):

    def setUp(self):
        self.cleaner = Cleaner()

    def test_remove_ref_type_1(self):
        text = '數學有着久遠的歷史。它被認為起源於[[人|人類]]早期的生產活動：[[中國]]古代的[[六藝|六艺]]之一就有「數」<ref>《' \
               '周礼·地官司徒·保氏》：「保氏掌谏王恶而养国子以道。乃教之六艺：一曰五礼，二曰六乐，三曰五射，四曰五驭，五曰六书，六' \
               '曰九数。」东汉的郑玄在他的《周礼注疏·地官司徒·保氏》中引郑司农（郑众）所言：「九数：方田、粟米、差分、少广、商功、' \
               '均输、方程、赢不足、旁要，今有重差、夕桀、勾股也。」</ref>，數學一詞在西方有[[希腊]]语[[詞源]]{{lang|el|μαθημα' \
               'τικός}}（mathematikós），意思是“学问的基础”，源于{{lang|el|μάθημα}}（máthema，“[[科学]]，知识，学问”）。'
        expected = '數學有着久遠的歷史。它被認為起源於[[人|人類]]早期的生產活動：[[中國]]古代的[[六藝|六艺]]之一就有「數」，數學' \
                   '一詞在西方有[[希腊]]语[[詞源]]{{lang|el|μαθηματικός}}（mathematikós），意思是“学问的基础”，源于' \
                   '{{lang|el|μάθημα}}（máthema，“[[科学]]，知识，学问”）。'
        actual = self.cleaner._remove_refs(text)
        self.assertEqual(expected, actual)

    def test_remove_ref_type_2(self):
        text = '这些新的哲学运动伴随着欧洲宗教和政治的剧变同时出现：[[宗教改革]]和[[封建制度_(歐洲)|封建制]]的衰落。虽然参与宗教' \
               '改革的神学家们对哲学没有直接的兴趣，他们打破了神学和知识权威的传统基础。同时还伴随着[[信仰主义]]和[[怀疑主义]]的' \
               '复兴，体现在[[德西德里乌斯·伊拉斯谟|伊拉斯谟]]，[[米歇尔·德·蒙泰涅|蒙泰涅]]和{{le|弗朗西斯科·桑切斯|Francisco' \
               ' Sanches|桑切斯}}等思想家身上<ref name=\"scepticism\"/><ref name=\"copleston\"/><ref name=\"' \
               'reformation\"/>。同时，[[民族国家]]政治上逐步的[[中央集权]]的过程得到了世俗政治哲学的响应，如[[尼可罗·' \
               '马基亚维利]]（常被描述为第一个现代政治思想家，或者是现代政治思想形成的关键点<ref name=\"Internet Encyclopedia ' \
               'of Philosophy\"/>）、[[托马斯·莫尔]]、[[德西德里乌斯·伊拉斯谟|伊拉斯谟]]、[[尤斯图斯·利普修斯]]、[[让·博丹]]' \
               '和[[胡果·格老秀斯]]等的著作<ref name=\"renaissance5\"/><ref name=\"renaissance6\"/><ref name=\"amencps' \
               '-25\" group=\"a\"/><ref name=\"brencps-25\" group=\"b\"/><ref name=\"cnencps-25\" group=\"d\"/>'
        expected = '这些新的哲学运动伴随着欧洲宗教和政治的剧变同时出现：[[宗教改革]]和[[封建制度_(歐洲)|封建制]]的衰落。虽然参与' \
                   '宗教改革的神学家们对哲学没有直接的兴趣，他们打破了神学和知识权威的传统基础。同时还伴随着[[信仰主义]]和[[怀疑' \
                   '主义]]的复兴，体现在[[德西德里乌斯·伊拉斯谟|伊拉斯谟]]，[[米歇尔·德·蒙泰涅|蒙泰涅]]和{{le|弗朗西斯科·' \
                   '桑切斯|Francisco Sanches|桑切斯}}等思想家身上。同时，[[民族国家]]政治上逐步的[[中央集权]]的过程得到了世俗' \
                   '政治哲学的响应，如[[尼可罗·马基亚维利]]（常被描述为第一个现代政治思想家，或者是现代政治思想形成的关键点）、' \
                   '[[托马斯·莫尔]]、[[德西德里乌斯·伊拉斯谟|伊拉斯谟]]、[[尤斯图斯·利普修斯]]、[[让·博丹]]和[[胡果·格老秀斯]]' \
                   '等的著作'
        actual = self.cleaner._remove_refs(text)
        self.assertEqual(expected, actual)

    def test_remove_ref_multiline(self):
        text = '[[史前史|史前]]的人類就已嘗試用自然的法則來衡量物質的多少、時間的長短等抽象的數量關係，比如[[时间单位]]有[[日]]、' \
               '[[季節]]和[[年]]等。[[算术|算術]]（[[加法|加]][[減法|減]][[乘法|乘]][[除法|除]]）也自然而然地產生了。古代的石' \
               '碑及泥版亦證實了當時已有[[几何学|幾何]]的知識<ref>{{Cite web \n |url= http://web.ptes.tp.edu.tw/big6/civ' \
               'il/babylonian-03.htm\n |title= 數學\n |accessdate=2013-10-06\n |publisher= 台北市立北投國小\n}}</ref>。'
        expected = '[[史前史|史前]]的人類就已嘗試用自然的法則來衡量物質的多少、時間的長短等抽象的數量關係，比如[[时间单位]]有[[日' \
                   ']]、[[季節]]和[[年]]等。[[算术|算術]]（[[加法|加]][[減法|減]][[乘法|乘]][[除法|除]]）也自然而然地產生了。' \
                   '古代的石碑及泥版亦證實了當時已有[[几何学|幾何]]的知識。'
        actual = self.cleaner._remove_refs(text)
        self.assertEqual(expected, actual)
