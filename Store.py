from Phone import Phone

class Store:
    def __init__(self, name):
        self.name = name
        self.inventory = []  # list of Phone objects

    # already done for you - look at how it loops through inventory
    def show_inventory(self):
        print(f"\n--- {self.name} ---")
        for phone in self.inventory:
            print(phone.display_info())

    # TODO 3: add phone to self.inventory
    def add_phone(self, phone):
        pass

    # TODO 4: find the phone with that model name, remove it from inventory, and return it
    # if no phone has that name, return None
    def sell_phone(self, model_name):
        pass

    # TODO 5: return the Phone with the lowest price
    # if inventory is empty, return None
    def find_cheapest(self):
        pass
