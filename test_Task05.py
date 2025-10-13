import unittest
from task5 import ticket_price

class TestTicketPrice(unittest.TestCase):
    def test_child(self):
        self.assertEqual(ticket_price(10), "Child ticket")
    def test_boundary_child(self):
        self.assertEqual(ticket_price(12), "Child ticket")
    def test_boundary_adult(self):
        self.assertEqual(ticket_price(13), "Adult ticket")
    def test_adult(self):
        self.assertEqual(ticket_price(30), "Adult ticket")
    def test_boundary_senior(self):
        self.assertEqual(ticket_price(65), "Senior ticket")
    def test_senior(self):
        self.assertEqual(ticket_price(100), "Senior ticket")
    def test_invalid(self):
        self.assertEqual(ticket_price(-1), "Invalid age")

if __name__ == '__main__':
    unittest.main()
