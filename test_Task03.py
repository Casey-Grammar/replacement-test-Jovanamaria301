import unittest
from unittest.mock import patch
from io import StringIO
from Task03 import main

class TestTask03(unittest.TestCase):

    @patch('builtins.input', return_value='0')
    @patch('sys.stdout', new_callable=StringIO)
    def test_below_min(self, mock_stdout, mock_input):
        """Test with 0 cups (below minimum)"""
        main()
        expected_output = "Drink more water!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='3')
    @patch('sys.stdout', new_callable=StringIO)
    def test_just_below_good(self, mock_stdout, mock_input):
        """Test with 3 cups (just below good range)"""
        main()
        expected_output = "Drink more water!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='4')
    @patch('sys.stdout', new_callable=StringIO)
    def test_min_good(self, mock_stdout, mock_input):
        """Test with 4 cups (minimum good amount)"""
        main()
        expected_output = "Good job staying hydrated!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='8')
    @patch('sys.stdout', new_callable=StringIO)
    def test_max_good(self, mock_stdout, mock_input):
        """Test with 8 cups (maximum good amount)"""
        main()
        expected_output = "Good job staying hydrated!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='9')
    @patch('sys.stdout', new_callable=StringIO)
    def test_above_good(self, mock_stdout, mock_input):
        """Test with 9 cups (above good range)"""
        main()
        expected_output = "thats a lot of water!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='100')
    @patch('sys.stdout', new_callable=StringIO)
    def test_large_number(self, mock_stdout, mock_input):
        """Test with large number of cups"""
        main()
        expected_output = "thats a lot of water!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
