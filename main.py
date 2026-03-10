from Phone import Phone
from Store import Store

iphone  = Phone("Apple",   "iPhone 14",  800, 128)
pixel   = Phone("Google",  "Pixel 8",    700, 128)
samsung = Phone("Samsung", "Galaxy S23", 600, 256)

store = Store("Logan's Cell Shop")
store.add_phone(iphone)
store.add_phone(pixel)
store.add_phone(samsung)

store.show_inventory()

iphone.upgrade_storage(128)
print(f"\nAfter upgrade: {iphone.display_info()}")

samsung.apply_discount(10)
print(f"After discount: {samsung.display_info()}")

sold = store.sell_phone("Pixel 8")
print(f"\nSold: {sold.display_info()}")

store.show_inventory()

cheapest = store.find_cheapest()
print(f"\nCheapest: {cheapest.display_info()}")
