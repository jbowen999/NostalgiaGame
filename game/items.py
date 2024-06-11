import json


class ItemManager:
    def __init__(self, item_file):
        with open(item_file, "r") as file:
            self.items = json.load(file)

    def get_item(self, item_id):
        return self.items.get(item_id)
