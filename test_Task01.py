import unittest
from unittest.mock import patch
from io import StringIO
from Task01 import main

class TestTask01(unittest.TestCase):

    @patch('builtins.input', return_value='Go')
    @patch('sys.stdout', new_callable=StringIO)
    def test_normal(self, mock_stdout, mock_input):
        """Test with the input 'Go'"""
        main()
        expected_output = "Go!Go!Go!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_string(self, mock_stdout, mock_input):
        """Test with empty string input"""
        main()
        expected_output = "!!!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='A')
    @patch('sys.stdout', new_callable=StringIO)
    def test_single_char(self, mock_stdout, mock_input):
        """Test with a single character 'A'"""
        main()
        expected_output = "A!A!A!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='Hi There')
    @patch('sys.stdout', new_callable=StringIO)
    def test_spaces(self, mock_stdout, mock_input):
        """Test with spaces in input"""
        main()
        expected_output = "Hi There!Hi There!Hi There!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='!')
    @patch('sys.stdout', new_callable=StringIO)
    def test_special_chars(self, mock_stdout, mock_input):
        """Test with special character '!'"""
        main()
        expected_output = "!!!!!!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
