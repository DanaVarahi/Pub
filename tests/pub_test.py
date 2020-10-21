import unittest
from src.drink import Drink
from src.customer import Customer
from src.pub import Pub
import pdb


class TestPub(unittest.TestCase):
    def setUp(self):

        self.customer1 = Customer('Duncan', 2000, 12)
        self.customer2 = Customer('Lucinda', 1000, 21)
        self.customer3 = Customer('Dana', 5000, 18)

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
        self.pub.add_cash_to_till(self.drinks[0].price)
        self.assertEqual(2550, self.pub.till)

    def test_check_customer_age_pass(self):
        answer = self.pub.check_customer_age(self.customer3)
        self.assertEqual(True, answer)

    def test_check_customer_age_pass_fail(self):
        answer = self.pub.check_customer_age(self.customer1)
        self.assertEqual(False, answer)

    def test_serve_customer(self):

        # self.assertEqual(False, self.pub.serve_customer(self.customer1))

        # check customer age takes customer returns true or false depending on age.
        # self.pub.add_cash_to_till(self.drinks[2].price)
        #    self.assertEqual(3250, self.pub.till)
