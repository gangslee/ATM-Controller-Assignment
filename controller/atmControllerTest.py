import unittest
import atmController
from bank import bank


class AtmControllerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.controller = atmController.AtmController(bank.Bank({"A1B2C3": {"pin": 123456, "accounts": {"MY": 1000}}}))

    # test get_accounts method
    def test1_get_accounts(self):
        print("\nTest01 get_accounts Started")

        # Test get accounts logic - Success
        get_accounts_test = self.controller.get_accounts("A1B2C3", 123456)
        self.assertEqual(get_accounts_test, {'MY': 1000}, print("get_accounts case - Success Logic"))

        # Test get accounts logic - Fail, wrong card_id
        get_accounts_test = self.controller.get_accounts("AAAAAA", 123456)
        self.assertIsNone(get_accounts_test, print("get_accounts case - Fail Logic, Wrong Card ID"))

        # Test get accounts logic - Fail, wrong pin
        get_accounts_test = self.controller.get_accounts("A1B2C3", 111111)
        self.assertIsNone(get_accounts_test, print("get_accounts case - Fail Logic, Wrong PIN"))

        print("Success get_accounts Test")

    # test select_accounts method
    def test2_select_accounts(self):
        print("\nTest02 select_account Started")

        # Test select accounts logic - Success
        select_account_test = self.controller.select_account("MY")
        self.assertTrue(select_account_test, print("select_account case - Success Logic"))

        # Test select accounts logic - Fail, wrong account
        select_account_test = self.controller.select_account("WRONG")
        self.assertFalse(select_account_test, print("select_account case - Fail Logic, Wrong Account"))

        print("Success select_account Test")

    # test see_balance method
    def test3_see_balance(self):
        print("\nTest03 see_balance Started")

        # Test see balance logic - Success
        see_balance_test = self.controller.see_balance("MY")
        self.assertEqual(see_balance_test, 1000, print("see_balance case - Success Logic"))

        # Test see balance logic - Fail
        see_balance_test = self.controller.see_balance("FAIL")
        self.assertIsNone(see_balance_test, print("see_balance case - Fail Logic"))

        print("Success see_balance Test")

    # test deposit method
    def test4_deposit(self):
        print("\nTest04 deposit Started")

        # Test deposit logic - Success
        deposit_test = self.controller.deposit("MY", 200)
        self.assertEqual(deposit_test, 1200, print("deposit case - Success Logic"))

        # Test deposit logic - Fail, wrong account
        deposit_test = self.controller.deposit("FAIL", 200)
        self.assertIsNone(deposit_test, print("deposit case - Fail Logic, wrong account"))

        # Test deposit logic - Fail, wrong cash amount
        deposit_test = self.controller.deposit("MY", -200)
        self.assertIsNone(deposit_test, print("deposit case - Fail Logic, wrong cash amount"))

        print("Success deposit Test")

    # test withdraw method
    def test5_withdraw(self):
        print("\nTest05 withdraw Started")

        # Test withdraw logic - Success
        deposit_test = self.controller.withdraw("MY", 200)
        self.assertEqual(deposit_test, 1000, print("deposit case - Success Logic"))

        # Test withdraw logic - Fail, wrong account
        deposit_test = self.controller.withdraw("FAIL", 200)
        self.assertIsNone(deposit_test, print("deposit case - Fail Logic, wrong account"))

        # Test withdraw logic - Fail, wrong cash amount
        deposit_test = self.controller.withdraw("MY", -200)
        self.assertIsNone(deposit_test, print("deposit case - Fail Logic, wrong cash amount"))

        # Test withdraw logic - Fail, cash amount over the balnace
        deposit_test = self.controller.withdraw("MY", 2000)
        self.assertIsNone(deposit_test, print("deposit case - Fail Logic, wrong cash amount"))

        print("Success withdraw Test")


if __name__ == '__main__':
    unittest.main(failfast=True)
