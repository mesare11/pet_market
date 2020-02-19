from pet_goods import pet_goods
from pet_items import pet_items
class pet_feeders(pet_items):
    def __init__(self, name, price, kind_item, expiration_date, feeder_for_kind_animal, feeder_size):
        pet_items.__init__(self, name, price, kind_item, expiration_date)
        self.feeder_for_kind_animal = feeder_for_kind_animal
        self.feeder_size = feeder_size

    def display_feeders(self):
        print(self.name, self.price, self.kind_item, self.expiration_date, self.feeder_for_kind_animal, self.feeder_size)
