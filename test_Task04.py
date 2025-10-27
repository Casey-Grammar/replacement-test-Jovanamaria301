import unittest
from unittest.mock import patch
from io import StringIO
from Task04 import main

class TestTask04(unittest.TestCase):

    @patch('builtins.input', return_value='3')
    @patch('sys.stdout', new_callable=StringIO)
    def test_three(self, mock_stdout, mock_input):
        """Test countdown from 3"""
        main()
        expected_output = "T-minus\nT-minus\nT-minus"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='1')
    @patch('sys.stdout', new_callable=StringIO)
    def test_one(self, mock_stdout, mock_input):
        """Test countdown from 1"""
        main()
        expected_output = "T-minus"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='0')
    @patch('sys.stdout', new_callable=StringIO)
    def test_zero(self, mock_stdout, mock_input):
        """Test countdown from 0 (should produce no output)"""
        main()
        expected_output = ""
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='-5')
    @patch('sys.stdout', new_callable=StringIO)
    def test_negative(self, mock_stdout, mock_input):
        """Test countdown from negative number (should produce no output)"""
        main()
        expected_output = ""
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
