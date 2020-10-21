class Pub:

    def __init__(self, name, drinks, till):
        self.name = name
        self.drinks = []
        self.till = till

    def add_cash_to_till(self, cash):
        self.till += cash

    def check_customer_age(self, customer):
        return customer.age >= 18

    # def serve_customer(self, customer):
    #     #  check customer age true/false
    #     #  removes money from the till
