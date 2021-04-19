import unittest
import atmController
from bank import bank


class AtmControllerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.controller = atmController.AtmController(bank.Bank(
            {"A1B2C3": {"pin": 123456, "accounts": {"MY": 1000}}}))

    # test get_accounts method
    def test1_get_accounts(self):
        print("\nTest01 get_accounts Started")

        # Test get accounts logic - Success
        get_accounts_test = self.controller.get_accounts("A1B2C3", 123456)
        self.assertEqual(get_accounts_test, ["MY"], print("get_accounts case - Success Logic"))

        # Test get accounts logic - Fail, wrong card_id
        get_accounts_test = self.controller.get_accounts("AAAAAA", 123456)
        self.assertIsNone(get_accounts_test, print("get_accounts case - Fail Logic, Wrong Card ID"))

        # Test get accounts logic - Fail, wrong pin
        get_accounts_test = self.controller.get_accounts("A1B2C3", 111111)
        self.assertIsNone(get_accounts_test, print("get_accounts case - Fail Logic, Wrong PIN"))

        print("Success get_accounts Test")

    def test2_select_accounts(self):
        print("\nTest02 select_account Started")

        # Test select accounts logic - Success
        select_account_test = self.controller.select_account("MY")
        self.assertTrue(select_account_test, print("select_account case - Success Logic"))

        # Test select accounts logic - Fail, wrong account
        select_account_test = self.controller.select_account("WRONG")
        self.assertFalse(select_account_test, print("select_account case - Fail Logic, Wrong Account"))

        print("Success select_account Test")


if __name__ == '__main__':
    unittest.main(failfast=True)
