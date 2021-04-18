import unittest
import bank


class BankTest(unittest.TestCase):
    def setUp(self):
        self.bank = bank.Bank(
            {"A1B2C3": {"pin": 123456, "accounts": {"My": 1000}}})

    # test add_data method
    def test1_add_data(self):
        print("\nTest01 add_data Started")

        # Test createable logic
        add_data_test = self.bank.add_data("TEST01", 111111, "LEE", 10000)
        self.assertTrue(add_data_test, print(
            "add_data case - Creatable Logic"))

        # Test non-createable logic
        add_data_test = self.bank.add_data("TEST01", 111111, "LEE", 500)
        self.assertFalse(add_data_test, print(
            "add_data case - Non-Creatable Logic, Data is already created"))

        print("Success add_data Test")

    # test add_account method
    def test2_add_account(self):
        print("\nTest02 add_account Started")

        add_account_test = self.bank.add_account("A1B2C3", 123456, "KIM", 3000)
        self.assertEqual(add_account_test, {'My': 1000, 'KIM': 3000}, print(
            "add_account case - Creatable Account"))


if __name__ == '__main__':
    unittest.main(failfast=True)
