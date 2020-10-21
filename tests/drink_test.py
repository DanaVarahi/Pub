import unittest
from src.drink import Drink


class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink('Guinness', 550)

    def test_drink_has_a_name(self):
        self.assertEqual('Guinness', self.drink.name)

    def test_drink_has_a_price(self):
        self.assertEqual(550, self.drink.price)
