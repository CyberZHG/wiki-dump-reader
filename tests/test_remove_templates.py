import unittest
from src import Cleaner


class TestRemoveTemplates(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.cleaner = Cleaner()

    def test_remove_templates(self):
        text = "'''数学'''是利用符号语言研究[[數量]]<ref name=\"OED\">{{cite web |url=http://oed.com/view/Entry/114974" \
               " |title=mathematics, ''n.'' |publisher=Oxford University Press |work=Oxford English Dictionary |ye" \
               "ar=2012 |accessdate=2012-07-16 |quote=The science of space, number, quantity, and arrangement, who" \
               "se methods involve logical reasoning and usually the use of symbolic notation, and which includes " \
               "geometry, arithmetic, algebra, and analysis.}}{{en}}</ref>、[[数学结构|结构]]<ref name=\"Kneebone\">{" \
               "{cite book |title=Mathematical Logic and the Foundations of Mathematics: An Introductory Survey |p" \
               "ublisher=Dover |author=Kneebone, G.T. |year=1963 |pages=[http://books.google.com/books?id=tCXxf4vb" \
               "XCcC&amp;pg=PA4 4] |isbn=0-486-41712-3 |quote=Mathematics ... is simply the study of abstract struc" \
               "tures, or formal patterns of connectedness.}}{{en}}</ref>、[[变化]]<ref name=\"LaTorre\">{{cite book" \
               " |title=Calculus Concepts: An Informal Approach to the Mathematics of Change |publisher=Cengage Le" \
               "arning |author=LaTorre, Donald R., John W. Kenelly, Iris B. Reed, Laurel R. Carpenter, and Cynthia" \
               " R Harris |year=2011 |pages=[http://books.google.com/books?id=1Ebu2Tij4QsC&amp;pg=PA2 2] |isbn=1-4" \
               "390-4957-2 |quote=Calculus is the study of change—how things change, and how quickly they change.}" \
               "}{{en}}</ref><ref name=\"Ramana\">{{cite book |title=Applied Mathematics |publisher=Tata McGraw–Hi" \
               "ll Education |author=Ramana |year=2007 |page=[http://books.google.com/books?id=XCRC6BeKhIIC&amp;pg" \
               "=SA2-PA10 2.10] |isbn=0-07-066753-5 |quote=The mathematical study of change, motion, growth or dec" \
               "ay is calculus.}}{{en}}</ref>以及[[空间 (数学)|空间]]<ref name=OED/>等概念的一門[[学科]]，从某种角度看屬於" \
               "[[形式科學]]的一種。數學透過[[抽象化]]和[[逻辑|邏輯]][[推理]]的使用，由[[計數]]、[[计算|計算]]、[[量度]]和對物" \
               "體[[形狀]]及[[運動 (物理學)|運動]]的觀察而產生。[[数学家|數學家]]們拓展這些概念，為了公式化新的[[猜想]]以及從選定" \
               "的[[公理]]及[[定義]]中建立起[[严谨 (数学)|嚴謹]]推導出的定理。<ref>Jourdain</ref>"
        expected = "'''数学'''是利用符号语言研究[[數量]]<ref name=\"OED\"></ref>、[[数学结构|结构]]<ref name=\"Kneebone\"" \
                   "></ref>、[[变化]]<ref name=\"LaTorre\"></ref><ref name=\"Ramana\"></ref>以及[[空间 (数学)|空间]]<re" \
                   "f name=OED/>等概念的一門[[学科]]，从某种角度看屬於[[形式科學]]的一種。數學透過[[抽象化]]和[[逻辑|邏輯]][[推" \
                   "理]]的使用，由[[計數]]、[[计算|計算]]、[[量度]]和對物體[[形狀]]及[[運動 (物理學)|運動]]的觀察而產生。[[数学" \
                   "家|數學家]]們拓展這些概念，為了公式化新的[[猜想]]以及從選定的[[公理]]及[[定義]]中建立起[[严谨 (数学)|嚴謹]]" \
                   "推導出的定理。<ref>Jourdain</ref>"
        actual = self.cleaner._remove_templates(text)
        self.assertEqual(expected, actual)

        text = "亚里士多德死后，整个哲学界陷入了独立时期，称为{{link-en|希腊化哲学|Hellenistic_philosophy}}时期。因为整个社会" \
               "和政治陷入混乱。这段时期产生了[[斯多葛学派]]和[[伊壁鸠鲁学派]]，以及[[皮浪主义|怀疑主义派]]、[[新柏拉图主义|新柏" \
               "拉图派]]和{{le|新毕达哥拉斯主义|Neopythagoreanism}}。这些学派的共同特点是伦理化。斯多葛学派主要是顺应自然和自制" \
               "。伊壁鸠鲁学派则是把快乐作为生活的本质和善的标准。而新柏拉图派和新毕达哥拉斯派都是带有[[宗教]]主义的哲学，并逐渐产" \
               "生融化[[基督教]]和希腊哲学于一体的理论，即为后来的[[基督教哲学]]。"
        expected = "亚里士多德死后，整个哲学界陷入了独立时期，称为希腊化哲学时期。因为整个社会和政治陷入混乱。这段时期产生了[[斯多葛" \
                   "学派]]和[[伊壁鸠鲁学派]]，以及[[皮浪主义|怀疑主义派]]、[[新柏拉图主义|新柏拉图派]]和新毕达哥拉斯主义。这些学" \
                   "派的共同特点是伦理化。斯多葛学派主要是顺应自然和自制。伊壁鸠鲁学派则是把快乐作为生活的本质和善的标准。而新柏拉图" \
                   "派和新毕达哥拉斯派都是带有[[宗教]]主义的哲学，并逐渐产生融化[[基督教]]和希腊哲学于一体的理论，即为后来的[[基督" \
                   "教哲学]]。"
        actual = self.cleaner._remove_templates(text)
        self.assertEqual(expected, actual)
