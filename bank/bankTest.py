import unittest
import bank


class BankTest(unittest.TestCase):
    def setUp(self):
        self.bank = bank.Bank(
            {"A1B2C3": {"pin": 123456, "accounts": {"MY": 1000}}})

    # test add_data method
    def test1_add_data(self):
        print("\nTest01 add_data Started")

        # Test creatable logic
        add_data_test = self.bank.add_data("TEST01", 111111, {"LEE": 10000})
        self.assertTrue(add_data_test, print(
            "add_data case - Creatable Logic"))

        # Test non-creatable logic
        add_data_test = self.bank.add_data("TEST01", 111111, {"LEE": 500})
        self.assertFalse(add_data_test, print(
            "add_data case - Non-Creatable Logic, Data is already created"))

        print("Success add_data Test")

    # test add_account method
    def test2_add_account(self):
        print("\nTest02 add_account Started")

        # Test addable logic
        add_account_test = self.bank.add_account("A1B2C3", 123456, "KIM")
        self.assertTrue(add_account_test, print(
            "add_account case - Creatable Account"))

        # Test non-addable logic - wrong card_id
        wrong_card_test = self.bank.add_account("AAAAAA", 123456, "KIM")
        self.assertFalse(wrong_card_test, print(
            "add_account case - Non-Creatable Account, Wrong Card ID"))

        # Test non-addable logic - wrong pin
        wrong_pin_test = self.bank.add_account("A1B2C3", 111111, "KIM")
        self.assertFalse(wrong_pin_test, print(
            "add_account case - Non-Creatable Account, Wrong PIN Number"))

        print("Success add_account Test")

    # test auth_info method
    def test3_auth_info(self):
        print("\nTest03 auth_info Started")

        # Test Authorization - Success
        auth_info_test = self.bank.auth_info("A1B2C3", 123456)
        self.assertEqual(auth_info_test, {'MY': 1000}, print("auth_info case - Authorization Success"))

        # Test Authorization - Fail
        auth_fail_test = self.bank.auth_info("AAAAAA", 111111)
        self.assertIsNone(auth_fail_test, print("auth_info case - Authorization Fail"))

        print("Success auth_info Test")

    # test update_data method
    def test4_update_data(self):
        print("\nTest04 update_data Started")

        # Test Update Data - Success
        update_data_test = self.bank.update_data("A1B2C3", 123456, "MY", 500)
        self.assertTrue(update_data_test,print("update_data case - Update Success"))

        # Test Update Data - Fail, wrong card_id
        update_data_test = self.bank.update_data("WRONG", 123456, "MY", 500)
        self.assertFalse(update_data_test,print("update_data case - Update Fail, Wrong Card ID"))

        # Test Update Data - Fail, wrong pin
        update_data_test = self.bank.update_data("A1B2C3", 111111, "MY", 500)
        self.assertFalse(update_data_test,print("update_data case - Update Fail, Wrong PIN Number"))

        # Test Update Data - Fail, wrong account
        update_data_test = self.bank.update_data("A1B2C3", 123456, "WRONG", 500)
        self.assertFalse(update_data_test,print("update_data case - Update Fail, Wrong Account"))

        # Test Update Data - Fail, wrong cash amount
        update_data_test = self.bank.update_data("A1B2C3", 123456, "MY", -500)
        self.assertFalse(update_data_test,print("update_data case - Update Fail, Wrong Cash Amount"))

        print("Success update_data Test")


if __name__ == '__main__':
    unittest.main(failfast=True)
