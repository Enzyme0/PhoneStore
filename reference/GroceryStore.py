from Phone import Phone

class GroceryStore:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def show_inventory(self):
        print(f"\n--- {self.name} ---")
        for vegetable in self.inventory:
            print(vegetable)

    def add_vegetable(self, phone):
        self.inventory.append("🥬")
        return None