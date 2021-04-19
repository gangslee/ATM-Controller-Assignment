class Bank():
    def __init__(self, data={}):
        self.data = data

    def add_data(self, card_id, pin, account, balance):
        if card_id not in self.data:
            self.data[card_id] = {"pin": pin, "accounts": {account: balance}}
            return True
        else:
            return False

    def add_account(self, card_id, pin, account):
        if card_id in self.data and pin == self.data[card_id]["pin"]:
            self.data[card_id]["accounts"][account] = 0
            return True
        else:
            return False

    def auth_info(self, card_id, pin):
        if card_id in self.data and pin == self.data[card_id]["pin"]:
            return list(self.data[card_id]["accounts"].keys())
        else:
            return None
