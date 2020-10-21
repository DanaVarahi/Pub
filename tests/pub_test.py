import unittest
from src.drink import Drink
from src.customer import Customer
from src.pub import Pub


class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink('Red Kite Ale', 250)
        self.drink2 = Drink("Gin  and tonic", 400)

        drinks = [self.drink1, self.drink2]
        self.pub = Pub("Alpaca Inn", drinks, 2000)

    def test_pub_has_name(self):
        self.assertEqual("Alpaca Inn", self.pub.name)
