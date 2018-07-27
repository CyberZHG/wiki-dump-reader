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
            'wikis',
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

    def test_broken(self):
        broken_files = ['zhwiki-broken-%d.xml' % i for i in range(1, 5)]
        for broken_file in broken_files:
            path = os.path.join(self.current_path, 'wikis', broken_file)
            for _ in iterate(path):
                self.assertTrue(False)

    def test_clean(self):
        targets = {
            '数学': 'Mathematics',
            '哲学': 'Philosophy',
            '文學': 'Literature',
        }
        for target_title, target in targets.items():
            found = False
            for title, text in iterate(self.sample_file_path):
                if title == target_title:
                    found = True
                    text = self.cleaner.clean_text(text)
                    actual, _ = self.cleaner.build_links(text)
                    expected = self.read_target(target)
                    if actual != expected:
                        self.save_temp(target, actual)
                    self.assertEqual(expected, actual, target)
                else:
                    text = self.cleaner.clean_text(text)
                    self.cleaner.build_links(text)
            self.assertTrue(found)
