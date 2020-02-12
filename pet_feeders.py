class pet_feeders(pet_items):
    def __init__(self, name, price, kind_item, expiration_date, feeder_for_kind_animal, feeder_size):
    pet_goods.__init__(self, name, price)
    pet_toys.__init__(self, kind_item, expiration_date)
    self.feeder_for_kind_animal = feeder_for_kind_animal
    self.feeder_size = feeder_size
