import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.test_data = Employee('William', 'Chia', 1000000)
    
    def test_give_default_raise(self):
        self.test_data.give_raise()
        self.assertEqual(1005000, self.test_data.money)

    def test_give_custom_raise(self):
        self.test_data.give_raise(money_plus = 50000)
        self.assertEqual(1050000, self.test_data.money)

unittest.main()