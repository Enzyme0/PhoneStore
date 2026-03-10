class Phone:
    def __init__(self, brand, model, price, storage):
        self.brand = brand
        self.model = model
        self.price = price
        self.storage = storage

    # already done for you - look at this to understand how methods work
    def display_info(self):
        return f"{self.brand} {self.model} - ${self.price}, {self.storage}GB"

    # TODO 1: add extra_gb to self.storage
    def upgrade_storage(self, extra_gb):
        pass

    # TODO 2: reduce self.price by percent
    # hint: if percent is 10, that means 10% off
    # hint: new price = price * (1 - percent / 100)
    def apply_discount(self, percent):
        pass
