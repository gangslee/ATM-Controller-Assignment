# 계좌 정보들을 갖고 있어야함

class Bank():
    def __init__(self):
        self.data = {}

    def add_data(self, card_id, pin, account, balance):
        if card_id not in self.data:
            self.data[card_id] = {"pin": pin, "accounts": {account: balance}}
            return True
        else:
            return False

    def add_account(self, card_id, account, balance):
        if card_id in self.data:
            self.data[card_id]["accoounts"][account][balance]
            return True
        else:
            return None

    def auth_info(self, card_id, pin):
        if card_id in self.data and pin == self.data[card_id]["pin"]:
            return self.data[card_id]["accounts"]
        else:
            return None
