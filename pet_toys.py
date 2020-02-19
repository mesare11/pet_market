from pet_goods import pet_goods
from pet_items import pet_items
class pet_toys(pet_items):
    def __init__(self, name, price, kind_item, expiration_date, toy_for_kind_animal, kind_of_toy):
        pet_items.__init__(self, name, price, kind_item, expiration_date)
        self.toy_for_kind_animal = toy_for_kind_animal
        self.kind_of_toy = kind_of_toy

    def display_toys(self):
        print(self.name, self.price, self.kind_item, self.expiration_date, self.toy_for_kind_animal, self.kind_of_toy)
