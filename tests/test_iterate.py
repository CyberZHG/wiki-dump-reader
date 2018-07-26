import os
import codecs
import unittest
from src import Cleaner, iterate


class TestIterate(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.cleaner = Cleaner()
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.sample_file_path = os.path.join(
            self.current_path,
            'zhwiki-test-pages.xml'
        )

    def read_target(self, name):
        path = os.path.join(self.current_path, 'targets', name + '.txt')
        with codecs.open(path, 'r', 'utf8') as reader:
            target = reader.read()
        return target

    def save_temp(self, name, text):
        path = os.path.join(self.current_path, 'targets', name + '.tmp')
        with codecs.open(path, 'w', 'utf8') as writer:
            writer.write(text)

    def test_clean_mathematics(self):
        found = False
        for title, text in iterate(self.sample_file_path):
            if title == '数学':
                found = True
                text = self.cleaner.clean_text(text)
                actual, _ = self.cleaner.build_links(text)
                expected = self.read_target('mathematics')
                if actual != expected:
                    self.save_temp('mathematics', actual)
                self.assertEqual(expected, actual)
        self.assertTrue(found)
