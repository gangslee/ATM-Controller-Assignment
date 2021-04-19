class AtmController():
    def __init__(self, bank):
        self.bank = bank
        self.accounts = None

    def get_accounts(self, bank, card_id, pin):
        accounts = self.bank.auth_info_test(card_id, pin)
        self.accounts = accounts
