import unittest
from Task01 import triple_cheer

class TestTripleCheer(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(triple_cheer("Go"), "Go!Go!Go")
    def test_empty_string(self):
        self.assertEqual(triple_cheer(""), "!!")
    def test_single_char(self):
        self.assertEqual(triple_cheer("A"), "A!A!A")
    def test_spaces(self):
        self.assertEqual(triple_cheer("Hi There"), "Hi There!Hi There!Hi There")
    def test_special_chars(self):
        self.assertEqual(triple_cheer("!"), "!!!")

if __name__ == '__main__':
    unittest.main()
