import unittest
from task4 import rocket_countdown

class TestRocketCountdown(unittest.TestCase):
    def test_three(self):
        self.assertEqual(rocket_countdown(3), ["T-minus 3", "T-minus 2", "T-minus 1"])
    def test_one(self):
        self.assertEqual(rocket_countdown(1), ["T-minus 1"])
    def test_zero(self):
        self.assertEqual(rocket_countdown(0), [])
    def test_negative(self):
        self.assertEqual(rocket_countdown(-5), [])

if __name__ == '__main__':
    unittest.main()
