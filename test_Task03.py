import unittest
from task3 import water_reminder

class TestWaterReminder(unittest.TestCase):
    def test_below_min(self):
        self.assertEqual(water_reminder(0), "Drink more water!")
    def test_just_below_good(self):
        self.assertEqual(water_reminder(3), "Drink more water!")
    def test_min_good(self):
        self.assertEqual(water_reminder(4), "Good job staying hydrated!")
    def test_max_good(self):
        self.assertEqual(water_reminder(8), "Good job staying hydrated!")
    def test_above_good(self):
        self.assertEqual(water_reminder(9), "That's a lot of water!")
    def test_large_number(self):
        self.assertEqual(water_reminder(100), "That's a lot of water!")

if __name__ == '__main__':
    unittest.main()
