import unittest
from src.drink import Drink
from src.customer import Customer
from src.pub import Pub
# from tests.pub_test import TestPub
import pdb


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer('David', 1000)
        self.customer2 = Customer('Lucy', 1500)

        drink1 = Drink("Guinness", 650)
        drink2 = Drink("Lager", 350)
        drink3 = Drink("Wine", 250)

        self.drinks = [drink1, drink2, drink3]
        self.pub = Pub('Green Goblin', self.drinks, 3000)

    def test_customer_has_name(self):
        self.assertEqual('David', self.customer1.name)

    def test_customer_has_money(self):
        self.assertEqual(1000, self.customer1.wallet)

    def test_remove_customer_cash(self):
        customer = self.customer1
        self.customer1.remove_customer_cash(self.drinks[2].price)
        self.assertEqual(750, self.customer1.wallet)

    def test_customer_can_buy_drink(self):

        self.customer1.remove_customer_cash(self.drinks[2].price)
        self.pub.add_cash_to_till(self.drinks[2].price)
        self.assertEqual(750, self.customer1.wallet)
        self.assertEqual(3250, self.pub.till)
