import unittest
from src.drink import Drink
from src.customer import Customer
from src.pub import Pub
import pdb


class TestPub(unittest.TestCase):
    def setUp(self):

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
