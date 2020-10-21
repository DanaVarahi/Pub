import unittest
from src.drink import Drink
from src.customer import Customer
from src.pub import Pub
import pdb


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer('David', 1000)
        self.customer2 = Customer('Lucy', 1500)

    def test_customer_has_name(self):
        self.assertEqual('David', self.customer1.name)

    def test_customer_has_money(self):
        self.assertEqual(1000, self.customer1.wallet)

    def test_remove_customer_cash(self):
        customer = self.customer1
        self.customer1.remove_customer_cash(50)
        self.assertEqual(950, self.customer1.wallet)
