import unittest
from task6 import full_months

class TestFullMonths(unittest.TestCase):
    def test_jan_mar_xyz(self):
        self.assertEqual(full_months(['Jan', 'Mar', 'Xyz']), ['January', 'March'])
    def test_empty(self):
        self.assertEqual(full_months([]), [])
    def test_all_invalid(self):
        self.assertEqual(full_months(['Xyz', 'Abc']), [])
    def test_case_sensitive(self):
        self.assertEqual(full_months(['jan', 'FEB']), [])
    def test_all_months(self):
        self.assertEqual(full_months(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']),
                         ['January','February','March','April','May','June','July','August','September','October','November','December'])
    def test_duplicates(self):
        self.assertEqual(full_months(['Jan', 'Jan', 'Feb']), ['January', 'January', 'February'])
    def test_one_month(self):
        self.assertEqual(full_months(['May']), ['May'])
    def test_last_month(self):
        self.assertEqual(full_months(['Dec']), ['December'])

if __name__ == '__main__':
    unittest.main()
