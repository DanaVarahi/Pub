import unittest
from src.drink import Drink
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer('David', 1000)

    def test_customer_has_name(self):
        self.assertEqual('David', self.customer.name)
