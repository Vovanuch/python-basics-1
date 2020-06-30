import unittest
from name_function import formatted_name

class NameTestCase(unittest.TestCase):
    
    def test_first_last_name(self):
        result = formatted_name('vasya', 'ivanov')
        self.assertEqual(result, 'Vasya Ivanov')
