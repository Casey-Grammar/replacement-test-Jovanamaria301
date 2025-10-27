import unittest
from unittest.mock import patch
from io import StringIO
from Task02 import main

class TestTask02(unittest.TestCase):

    @patch('builtins.input', return_value='dog')
    @patch('sys.stdout', new_callable=StringIO)
    def test_dog_lower(self, mock_stdout, mock_input):
        """Test with lowercase 'dog' input"""
        main()
        expected_output = "Woof!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='CAT')
    @patch('sys.stdout', new_callable=StringIO)
    def test_cat_upper(self, mock_stdout, mock_input):
        """Test with uppercase 'CAT' input"""
        main()
        expected_output = "Meow!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='Cow')
    @patch('sys.stdout', new_callable=StringIO)
    def test_cow_title(self, mock_stdout, mock_input):
        """Test with title case 'Cow' input"""
        main()
        expected_output = "Moo!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='duck')
    @patch('sys.stdout', new_callable=StringIO)
    def test_unknown(self, mock_stdout, mock_input):
        """Test with unknown animal 'duck'"""
        main()
        expected_output = "Unknown sound"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value=' dog ')
    @patch('sys.stdout', new_callable=StringIO)
    def test_leading_trailing_spaces(self, mock_stdout, mock_input):
        """Test with leading and trailing spaces"""
        main()
        expected_output = "Unknown sound"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_string(self, mock_stdout, mock_input):
        """Test with empty string input"""
        main()
        expected_output = "Unknown sound"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
