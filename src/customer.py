class Customer:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def remove_customer_cash(self, cash):
        self.wallet -= cash
