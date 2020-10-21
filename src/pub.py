class Pub:

    def __init__(self, name, drinks, till):
        self.name = name
        self.drinks = []
        self.till = till

    def add_cash_to_till(self, cash):
        self.till += cash
