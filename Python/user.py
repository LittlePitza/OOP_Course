from account import Account


class User(Account):
    def __init__(self, name, password, document, email):
        super().__init__(name, password)
        self.car = None
