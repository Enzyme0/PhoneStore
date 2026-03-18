import unittest
import os
import tempfile
from Phone import Phone
from Store import Store

# run with: python tests.py


class TestPhone(unittest.TestCase):

    def test_display_info(self):
        p = Phone("Apple", "iPhone 14", 800, 128)
        self.assertEqual(p.display_info(), "Apple iPhone 14 - $800, 128GB")

    def test_upgrade_storage(self):
        p = Phone("Apple", "iPhone 14", 800, 128)
        p.upgrade_storage(128)
        self.assertEqual(p.storage, 256)

    def test_upgrade_storage_again(self):
        p = Phone("Google", "Pixel 8", 700, 128)
        p.upgrade_storage(256)
        self.assertEqual(p.storage, 384)

    def test_apply_discount(self):
        p = Phone("Apple", "iPhone 14", 800, 128)
        p.apply_discount(10)
        self.assertAlmostEqual(p.price, 720.0)

    def test_apply_discount_half_off(self):
        p = Phone("Samsung", "Galaxy S23", 600, 256)
        p.apply_discount(50)
        self.assertAlmostEqual(p.price, 300.0)


class TestStore(unittest.TestCase):

    def setUp(self):
        self.store = Store("Test Shop")
        self.iphone  = Phone("Apple",   "iPhone 14",  800, 128)
        self.pixel   = Phone("Google",  "Pixel 8",    700, 128)
        self.samsung = Phone("Samsung", "Galaxy S23", 600, 256)

    def test_inventory_starts_empty(self):
        self.assertEqual(self.store.inventory, [])

    def test_add_phone(self):
        self.store.add_phone(self.iphone)
        self.assertIn(self.iphone, self.store.inventory)

    def test_add_multiple_phones(self):
        self.store.add_phone(self.iphone)
        self.store.add_phone(self.pixel)
        self.assertEqual(len(self.store.inventory), 2)

    def test_sell_phone_returns_it(self):
        self.store.add_phone(self.iphone)
        sold = self.store.sell_phone("iPhone 14")
        self.assertEqual(sold, self.iphone)

    def test_sell_phone_removes_from_inventory(self):
        self.store.add_phone(self.iphone)
        self.store.sell_phone("iPhone 14")
        self.assertNotIn(self.iphone, self.store.inventory)

    def test_sell_phone_not_found(self):
        result = self.store.sell_phone("iPhone 14")
        self.assertIsNone(result)

    def test_find_cheapest(self):
        self.store.add_phone(self.iphone)   # $800
        self.store.add_phone(self.pixel)    # $700
        self.store.add_phone(self.samsung)  # $600
        self.assertEqual(self.store.find_cheapest(), self.samsung)

    def test_find_cheapest_empty(self):
        self.assertIsNone(self.store.find_cheapest())

    def test_save_and_load_json_round_trip(self):
        self.store.add_phone(self.iphone)
        self.store.add_phone(self.pixel)

        fd, file_path = tempfile.mkstemp(suffix=".json")
        os.close(fd)
        try:
            self.store.save_to_json(file_path)
            loaded_store = Store.load_from_json(file_path)
        finally:
            os.remove(fd)

        self.assertEqual(loaded_store.name, self.store.name)
        self.assertEqual(len(loaded_store.inventory), 2)
        self.assertEqual(loaded_store.inventory[0].model, "iPhone 14")
        self.assertEqual(loaded_store.inventory[1].model, "Pixel 8")


if __name__ == "__main__":
    unittest.main(verbosity=2)
