import unittest
from unittest.mock import patch
from io import StringIO
from Task06 import main

class TestTask06(unittest.TestCase):

    @patch('builtins.input', return_value='Jan')
    @patch('sys.stdout', new_callable=StringIO)
    def test_jan(self, mock_stdout, mock_input):
        """Test with 'Jan' input"""
        main()
        expected_output = "January"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='Mar')
    @patch('sys.stdout', new_callable=StringIO)
    def test_mar(self, mock_stdout, mock_input):
        """Test with 'Mar' input"""
        main()
        expected_output = "March"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='Xyz')
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid(self, mock_stdout, mock_input):
        """Test with invalid month 'Xyz'"""
        main()
        expected_output = "Unrecognized month name"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='jan')
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_sensitive_lower(self, mock_stdout, mock_input):
        """Test case sensitivity with lowercase 'jan'"""
        main()
        expected_output = "Unrecognized month name"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='FEB')
    @patch('sys.stdout', new_callable=StringIO)
    def test_case_sensitive_upper(self, mock_stdout, mock_input):
        """Test case sensitivity with uppercase 'FEB'"""
        main()
        expected_output = "Unrecognized month name"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='May')
    @patch('sys.stdout', new_callable=StringIO)
    def test_may(self, mock_stdout, mock_input):
        """Test with 'May' (which stays 'May')"""
        main()
        expected_output = "May"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='Dec')
    @patch('sys.stdout', new_callable=StringIO)
    def test_dec(self, mock_stdout, mock_input):
        """Test with 'Dec' input"""
        main()
        expected_output = "December"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='Nov')
    @patch('sys.stdout', new_callable=StringIO)
    def test_feb(self, mock_stdout, mock_input):
        """Test with 'Nov' input"""
        main()
        expected_output = "November"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
