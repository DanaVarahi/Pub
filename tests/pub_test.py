import unittest
from src.drink import Drink
from src.customer import Customer
from src.pub import Pub
import pdb


class TestPub(unittest.TestCase):
    def setUp(self):

        self.customer1 = Customer('Duncan', 2000)
        self.customer2 = Customer('Lucinda', 1000)

        drink1 = Drink("Guinness", 550)
        drink2 = Drink("Lager", 250)
        drink3 = Drink("Wine", 150)

        self.drinks = [drink1, drink2, drink3]

        self.pub = Pub("Alpaca Inn", self.drinks, 2000)

    def test_pub_has_name(self):
        self.assertEqual("Alpaca Inn", self.pub.name)

    def test_pub_has_drinks(self):
        self.assertEqual(3, len(self.drinks))

    def test_pub_has_till(self):

        self.assertEqual(2000, self.pub.till)

    def test_add_cash_to_till(self):
        # pdb.set_trace()
        self.pub.add_cash_to_till(self.drinks[0].price)
        self.assertEqual(2550, self.pub.till)

    def test_can_sell_drink_to_customer(self):

        self.customer1.remove_customer_cash(self.drinks[2].price)
        self.pub.add_cash_to_till(self.drinks[2].price)
        self.assertEqual(1850, self.customer1.wallet)
        self.assertEqual(2150, self.pub.till)
