class pet_toys(pet_items):
    def __init__(self, name, price, kind_item, expiration_date, toy_for_kind_animal, kind_of_toy):
    pet_goods.__init__(self, name, price)
    pet_toys.__init__(self, kind_item, expiration_date)
    self.toy_for_kind_animal = toy_for_kind_animal
    self.kind_of_toy = kind_of_toy
