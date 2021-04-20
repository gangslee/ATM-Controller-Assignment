class Bank:
    def __init__(self, data=None):
        if data is None:
            data = {}
        self.data = data

    # Add new data(card_id, pin, accounts)
    def add_data(self, card_id, pin, accounts_info):
        if card_id not in self.data:
            self.data[card_id] = {"pin": pin, "accounts": accounts_info}
            return True
        else:
            return False

    # Add new account of exist card_id & pin
    def add_account(self, card_id, pin, account):
        if card_id in self.data and pin == self.data[card_id]["pin"]:
            self.data[card_id]["accounts"][account] = 0
            return True
        else:
            return False

    # Authorize input info
    def auth_info(self, card_id, pin):
        if card_id in self.data and pin == self.data[card_id]["pin"]:
            return self.data[card_id]["accounts"]
        else:
            return None

    # Update account data
    def update_data(self, card_id, pin, account, cash):
        if card_id in self.data and pin == self.data[card_id]["pin"]:
            if account in self.data[card_id]["accounts"] and cash >= 0:
                self.data[card_id]["accounts"][account] = cash
                return True
            else:
                return False
        else:
            return False
