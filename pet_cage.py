class pet_cage(pet_goods):
    def __init__(self, name, price, cage_for_kind_animal, size):
    pet_goods.__init__(self, name, price)
    self.cage_for_kind_animal = cage_for_kind_animal
    self.size = size
