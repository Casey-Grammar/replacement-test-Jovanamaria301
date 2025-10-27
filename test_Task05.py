import unittest
from unittest.mock import patch
from io import StringIO
from Task05 import main

class TestTask05(unittest.TestCase):

    @patch('builtins.input', return_value='10')
    @patch('sys.stdout', new_callable=StringIO)
    def test_child(self, mock_stdout, mock_input):
        """Test with child age (10)"""
        main()
        expected_output = "Child ticket"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='12')
    @patch('sys.stdout', new_callable=StringIO)
    def test_boundary_child(self, mock_stdout, mock_input):
        """Test with boundary child age (12)"""
        main()
        expected_output = "Child ticket"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='13')
    @patch('sys.stdout', new_callable=StringIO)
    def test_boundary_adult(self, mock_stdout, mock_input):
        """Test with boundary adult age (13)"""
        main()
        expected_output = "Adult ticket"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='30')
    @patch('sys.stdout', new_callable=StringIO)
    def test_adult(self, mock_stdout, mock_input):
        """Test with adult age (30)"""
        main()
        expected_output = "Adult ticket"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='65')
    @patch('sys.stdout', new_callable=StringIO)
    def test_boundary_senior(self, mock_stdout, mock_input):
        """Test with boundary senior age (65)"""
        main()
        expected_output = "Senior ticket"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='100')
    @patch('sys.stdout', new_callable=StringIO)
    def test_senior(self, mock_stdout, mock_input):
        """Test with senior age (100)"""
        main()
        expected_output = "Senior ticket"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='-1')
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid(self, mock_stdout, mock_input):
        """Test with invalid age (-1)"""
        main()
        expected_output = "invalid age"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
