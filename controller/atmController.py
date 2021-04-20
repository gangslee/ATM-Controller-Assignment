class AtmController:
    def __init__(self, bank):
        self.bank = bank
        self.card_id = None
        self.pin = None
        self.accounts = None

    # Get accounts from bank
    def get_accounts(self, card_id, pin):
        accounts = self.bank.auth_info(card_id, pin)

        if accounts:
            self.card_id = card_id
            self.pin = pin
            self.accounts = accounts
        return accounts

    # Select accounts which will used
    def select_account(self, account):
        if account in self.accounts:
            return True
        else:
            return False

    # See balance of selected account
    def see_balance(self, account):
        if account in self.accounts:
            return self.accounts[account]
        else:
            return None

    # Deposit cash from selected account
    def deposit(self, account, cash):
        if account in self.accounts:
            if cash > 0:
                self.accounts[account] += cash
                check_bank_update = self.bank.update_data(self.card_id, self.pin, account, self.accounts[account])

                if check_bank_update:
                    return self.accounts[account]
                else:
                    return None
            else:
                return None
        else:
            return None

    # Withdraw cash from selected account
    def withdraw(self, account, cash):
        if account in self.accounts:
            if 0 < cash <= self.accounts[account]:
                self.accounts[account] -= cash
                check_bank_update = self.bank.update_data(self.card_id, self.pin, account, self.accounts[account])

                if check_bank_update:
                    return self.accounts[account]
                else:
                    return None
            else:
                return None
        else:
            return None
