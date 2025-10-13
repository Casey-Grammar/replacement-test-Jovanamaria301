import unittest
from task2 import animal_sound

class TestAnimalSound(unittest.TestCase):
    def test_dog_lower(self):
        self.assertEqual(animal_sound("dog"), "Woof!")
    def test_cat_upper(self):
        self.assertEqual(animal_sound("CAT"), "Meow!")
    def test_cow_title(self):
        self.assertEqual(animal_sound("Cow"), "Moo!")
    def test_unknown(self):
        self.assertEqual(animal_sound("duck"), "Unknown sound")
    def test_leading_trailing_spaces(self):
        self.assertEqual(animal_sound(" dog "), "Unknown sound")
    def test_empty_string(self):
        self.assertEqual(animal_sound(""), "Unknown sound")

if __name__ == '__main__':
    unittest.main()
