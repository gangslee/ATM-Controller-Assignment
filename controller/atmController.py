class AtmController:
    def __init__(self, bank):
        self.bank = bank
        self.accounts = None

    def get_accounts(self, card_id, pin):
        accounts = self.bank.auth_info(card_id, pin)

        if accounts:
            self.accounts = accounts
        return accounts

    def select_account(self, account):
        if account in self.accounts:
            return True
        else:
            return False
