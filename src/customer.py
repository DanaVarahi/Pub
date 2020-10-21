class Customer:

    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age

    def remove_customer_cash(self, cash):
        self.wallet -= cash

        # buy drink method (removes price of a drink)
